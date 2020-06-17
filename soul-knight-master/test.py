import pygame
import os
import sys
from math import ceil, atan, degrees, sin, radians
from random import randint


def load_image(name, colorkey=None):
    # 图像加载功能
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def playing_song(name):
    # 音乐功能
    pygame.mixer.music.load(os.path.join('data', name))
    pygame.mixer.music.play(-1)


def playing_sound(name):
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.mixer.init()
    if proof_for_sound:
        audio = pygame.mixer.Sound(os.path.join('data', name))
        audio.play()


def terminate():
    pygame.quit()
    sys.exit()


def create_particles(quantity, coords):
    for _ in range(quantity):
        Particle(coords)
    # 粒子生成函数


def finish_screen():
    # 胜利窗口函数
    global open_finish_screen, open_start_screen
    fon_info = pygame.transform.scale(load_image('fon_for_finish.png'), (WIDTH, HEIGHT))
    screen.blit(fon_info, (0, 0))
    open_finish_screen = False
    pygame.mixer.music.pause()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and 240 >= pygame.mouse.get_pos()[0] >= 173 and \
                        324 >= pygame.mouse.get_pos()[1] >= 298:
                    open_start_screen = True
                    return
                elif event.button == 1 and 325 >= pygame.mouse.get_pos()[0] >= 250 and \
                        324 >= pygame.mouse.get_pos()[1] >= 298:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


def how_to_play_screen():
    # 控制窗口功能
    fon_info = pygame.transform.scale(load_image('fon_how_to_play.png'), (WIDTH, HEIGHT))
    screen.blit(fon_info, (0, 0))
    intro_text = ["说明: ",
                  "W-向上，S-向下",
                  "D - 向右, A - 向左",
                  "F - 挑选物品",
                  "LMB - 射击：",
                  "SPACE - 转移到另一个地图",
                  "转到",
                  "下一个地图，你要杀了。",
                  "一切敌人"]
    font = pygame.font.Font(None, 35)
    text_coord = 80
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 30
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and pygame.mouse.get_pos()[0] >= 439 and pygame.mouse.get_pos()[1] <= 30:
                    return
        pygame.display.flip()
        clock.tick(FPS)


def info_screen():
    # 游戏情节窗口功能
    fon_info = pygame.transform.scale(load_image('fon_info.png'), (WIDTH, HEIGHT))
    screen.blit(fon_info, (0, 0))
    intro_text = ["很久以前，阿萨辛家族 ",
                  "生活在幸福与和平,",
                  "但有一次", "一个疯狂的国王的军队攻击了一个氏族。",
                  "只有一个氏族的领袖还活着。",
                  "从那时起，他答应过自己……",
                  "直到他报仇，他不会平静下来,",
                  "为你的同胞。"]
    font = pygame.font.Font(None, 35)
    text_coord = 80
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 30
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and pygame.mouse.get_pos()[0] <= 61 and pygame.mouse.get_pos()[1] <= 31:
                    return
        pygame.display.flip()
        clock.tick(FPS)


def pause():
    # 游戏暂停和菜单功能
    global proof_for_song, proof_for_sound, l, h, r, d, running, open_start_screen, move_map
    tiles_group.draw(screen)
    potion_group.draw(screen)
    walls_group.draw(screen)
    weapons_group.draw(screen)
    enemy_group.draw(screen)
    enemy_weapon_group.draw(screen)
    portal_group.draw(screen)
    player_group.draw(screen)
    enemy_projectile.draw(screen)
    hero_projectile.draw(screen)
    hero_weapon_group.draw(screen)
    hwalls_group.draw(screen)
    screen.blit(Panel().image, (0, HEIGHT - 80))
    clock.tick(FPS)
    if proof_for_song:
        screen.blit(image_song_on, (160, HEIGHT - 40))
    else:
        screen.blit(image_song_off, (160, HEIGHT - 40))
    if proof_for_sound:
        screen.blit(image_sound_on, (160, HEIGHT - 80))
    else:
        screen.blit(image_sound_off, (160, HEIGHT - 80))
    menu = pygame.transform.scale(load_image('menu.png'), (100, 95))
    exit = pygame.transform.scale(load_image('exit.png'), (40, 40))
    retry = pygame.transform.scale(load_image('retry.png'), (40, 40))
    to_menu = pygame.transform.scale(load_image('to_exit_to_menu.png'), (90, 40))
    screen.blit(menu, (185, 205))
    screen.blit(exit, (190, 210))
    screen.blit(retry, (240, 210))
    screen.blit(to_menu, (190, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_a:
                    l = True
                elif event.key == pygame.K_w:
                    h = True
                elif event.key == pygame.K_s:
                    d = True
                elif event.key == pygame.K_d:
                    r = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    l = False
                elif event.key == pygame.K_w:
                    h = False
                elif event.key == pygame.K_s:
                    d = False
                elif event.key == pygame.K_d:
                    r = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1 and 190 <= pygame.mouse.get_pos()[0] <= 230 and
                        210 <= pygame.mouse.get_pos()[1] <= 250):
                    terminate()
                elif (event.button == 1 and 240 <= pygame.mouse.get_pos()[0] <= 280 and
                        210 <= pygame.mouse.get_pos()[1] <= 250):
                    open_start_screen = False
                    running = False
                    return
                elif (event.button == 1 and 190 <= pygame.mouse.get_pos()[0] <= 280 and
                        255 <= pygame.mouse.get_pos()[1] <= 295):
                    running = False
                    open_start_screen = True
                    move_map = False
                    pygame.mixer.music.pause()
                    return
                if event.button == 1:
                    if 160 < pygame.mouse.get_pos()[0] < 200 and HEIGHT - 40 <= pygame.mouse.get_pos()[1] <= HEIGHT:
                        if proof_for_song:
                            pygame.mixer.music.pause()
                            proof_for_song = False
                        else:
                            pygame.mixer.music.unpause()
                            proof_for_song = True
                    elif 160 < pygame.mouse.get_pos()[0] < 200 \
                            and HEIGHT - 80 <= pygame.mouse.get_pos()[1] < HEIGHT - 40:
                        if proof_for_sound:
                            proof_for_sound = False
                        else:
                            proof_for_sound = True
        if proof_for_song:
            screen.blit(image_song_on, (160, HEIGHT - 40))
        else:
            screen.blit(image_song_off, (160, HEIGHT - 40))
        if proof_for_sound:
            screen.blit(image_sound_on, (160, HEIGHT - 80))
        else:
            screen.blit(image_sound_off, (160, HEIGHT - 80))
        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    # 开始菜单
    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1 and 105 <= pygame.mouse.get_pos()[0] <= 393 and
                        113 <= pygame.mouse.get_pos()[1] <= 397):
                    return
                elif event.button == 1 and pygame.mouse.get_pos()[0] <= 61 and pygame.mouse.get_pos()[1] <= 31:
                    info_screen()
                    screen.blit(fon, (0, 0))
                elif event.button == 1 and pygame.mouse.get_pos()[0] >= 337 and pygame.mouse.get_pos()[1] <= 29:
                    how_to_play_screen()
                    screen.blit(fon, (0, 0))
                elif event.button == 1 and 134 >= pygame.mouse.get_pos()[0] >= 63 and pygame.mouse.get_pos()[1] <= 31:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    # 打开文本功能
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]
    max_width = max(map(len, level_map))
    level_map = list(map(lambda x: x.ljust(max_width, " "), level_map))
    return level_map


def generate_level(level):
    #创建地图精灵的函数
    global laser_max_size, move_map
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall1', x, y)
                Tile('d_wall', x, y)
                if y != len(level) - 1 and level[y + 1][x] == '#':
                    Tile('wall1', x, y + 0.5)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                px, py = x, y
            elif level[y][x] == '%':
                Tile('empty', x, y)
                Tile("portal", x, y)
    laser_max_size = int((len(max(level, key=lambda x: len(x))) ** 2 + len(level) ** 2) ** 0.5)
    new_player = Player(px, py)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Tile('wall', x, y)
    if not move_map:
        return new_player, px, py
    else:
        return new_player


class Tile(pygame.sprite.Sprite):
    # 墙壁和地板的类，地图，静态的东西。
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        if tile_type == 'wall1':
            walls_group.add(self)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        elif tile_type == "wall":
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y - 16)
            hwalls_group.add(self)
        elif tile_type == "d_wall":
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y + 16)
        elif tile_type == "portal":
            portal_group.add(self)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        else:
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    # 男主角阶级
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.f = True
        self.next_level = True
        self.coins = 0
        self.regulator = 0
        self.regenerator = -1
        self.fire = True
        self.brake = 0
        self.imagedeath = player_death
        self.c = 0
        self.health = HEALTH
        self.protection = PROTECTION
        self.bullets = BULLETS
        if pygame.mouse.get_pos()[0] > tile_width * pos_x + 18:#左右交换图片
            self.image = player_image
        else:
            self.image = player_image1
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.number_of_weapon = 0
        self.weapons = [colt]
        self.weapon = self.weapons[self.number_of_weapon]
        self.weapon.remove(weapons_group)
        hero_weapon_group.add(self.weapon)

    def animation(self):
        # 玩家的武器和动画扭转函数
        if self.health > 0:
            if pygame.mouse.get_pos()[0] > self.rect.x + 18:
                self.weapon.rect.topleft = (self.rect.x + WEAPON_X - self.weapon.butt, self.rect.y + WEAPON_Y)
                x_distance = pygame.mouse.get_pos()[0] - self.weapon.rect.x
                if x_distance == 0:
                    if pygame.mouse.get_pos()[1] > self.rect.y:
                        angle = 90
                    else:
                        angle = -90
                else:
                    angle = degrees(atan((self.weapon.rect.y - pygame.mouse.get_pos()[1]) / x_distance))
                    angle = degrees(atan((self.weapon.rect.y - (self.weapon.rect.h - self.weapon.rect.w) * sin(
                        radians(angle)) - pygame.mouse.get_pos()[1]) / x_distance))
                self.weapon.image = pygame.transform.rotate(self.weapon.main_image, angle)
                if pygame.mouse.get_pos()[1] < self.weapon.rect.y:
                    self.weapon.rect = self.weapon.rect.move(0, (self.weapon.rect.h - self.weapon.rect.w) * sin(
                        radians(angle)))
            else:
                self.weapon.rect.topright = (self.rect.x - WEAPON_X + self.weapon.butt + self.rect.w,
                                              self.rect.y + WEAPON_Y)
                x_distance = pygame.mouse.get_pos()[0] - self.weapon.rect.topright[0]
                if x_distance == 0:
                    if pygame.mouse.get_pos()[1] > self.rect.y:
                        angle = -90
                    else:
                        angle = 90
                else:
                    angle = degrees(atan((self.weapon.rect.y - pygame.mouse.get_pos()[1]) / x_distance))
                    angle = degrees(atan((self.weapon.rect.y - (self.weapon.rect.h - self.weapon.rect.w) * sin(
                        radians(angle)) - pygame.mouse.get_pos()[1]) / x_distance))
                self.weapon.image = pygame.transform.rotate(self.weapon.main_image1, angle)
                if pygame.mouse.get_pos()[1] < self.weapon.rect.y:
                    self.weapon.rect = self.weapon.rect.move(0, (self.weapon.rect.w - self.weapon.rect.h) * sin(
                        radians(angle)))
                    self.weapon.rect = self.weapon.rect.move(
                        -(self.weapon.rect.w - self.weapon.rect.h) * sin(radians(angle)), 0)
                else:
                    self.weapon.rect = self.weapon.rect.move(
                        (self.weapon.rect.w - self.weapon.rect.h) * sin(radians(angle)), 0)
            if r or l or h or d:
                if self.c < 25:
                    if pygame.mouse.get_pos()[0] > self.rect.x + 18:
                        self.image = player_animation[0]
                    else:
                        self.image = player_animation1[0]
                elif self.c < 50:
                    if pygame.mouse.get_pos()[0] > self.rect.x + 18:
                        self.image = player_animation[1]
                    else:
                        self.image = player_animation1[1]
                else:
                    self.c = -1
                self.c += 1
            else:
                self.c = 0
                if pygame.mouse.get_pos()[0] > self.rect.x + 18:
                    self.image = player_image
                else:
                    self.image = player_image1

    def update(self):
        # 玩家移动函数
        if self.health > 0:
            if l:
                self.rect.x -= 1
                if pygame.sprite.spritecollideany(self, walls_group):
                    self.rect.x += 1
            if h:
                self.rect.y -= 1
                if pygame.sprite.spritecollideany(self, walls_group):
                    self.rect.y += 1
            if d:
                self.rect.y += 1
                if pygame.sprite.spritecollideany(self, walls_group):
                    self.rect.y -= 1
            if r:
                self.rect.x += 1
                if pygame.sprite.spritecollideany(self, walls_group):
                    self.rect.x -= 1
            if not self.fire:
                self.brake += 1
                if self.brake >= FPS // self.weapon.rate_of_fire:
                    self.fire = True
            for projectile in enemy_projectile:
                if pygame.sprite.collide_mask(self, projectile):
                    if projectile.type_of_projectile == 'bullet':
                        self.regenerator = -1
                        self.regulator = -1
                        self.health = max(0, min(self.health + self.protection - projectile.damage, self.health))
                        self.protection = max(0, self.protection - projectile.damage)
                        playing_sound("for_gun_1.ogg")
                        projectile.kill()
                    elif projectile.proof_for_damage:
                        self.regenerator = -1
                        self.regulator = -1
                        self.health = max(0, min(self.health + self.protection - projectile.damage, self.health))
                        self.protection = max(0, self.protection - projectile.damage)
            if self.regulator == 5 * FPS:
                self.regenerator = (self.regenerator + 1) % (2 * FPS)
            else:
                self.regulator += 1
            if self.regenerator == 2 * FPS - 1 and self.protection != PROTECTION:
                self.protection += 1
        else:
            if self.f:
                self.rect = self.rect.move(0, self.rect.h - self.imagedeath.get_rect().h)
                self.image = self.imagedeath
                self.f = False

    def portal(self):
        # 进入下一关函数
        global open_start_screen, move_map, running, open_finish_screen
        proof_for_portal = True
        for j in enemy_group:
            if j.health > 0:
                proof_for_portal = False
        if proof_for_portal:
            if not move_map:
                for i in portal_group:
                    if pygame.sprite.collide_mask(self, i):
                        open_start_screen = False
                        move_map = True
                        running = False
            else:
                open_finish_screen = True
                open_start_screen = True
                move_map = False
                running = False

    def shot(self):
        # 射计函数
        if self.health > 0:
            if self.bullets >= self.weapon.cost and self.fire:
                player.bullets -= player.weapon.cost
                self.brake = 0
                hero_projectile.add(Projectile(self.weapon.type_of_projectile, self.weapon.rect.center,
                                               pygame.mouse.get_pos(), self.weapon.color, self.weapon.damage))
                self.fire = False


class Camera:
    # 负责跟踪玩家摄像头的班级。
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


class Panel:
    # 显示主角状态的类
    def __init__(self):
        font = pygame.font.Font(None, 24)
        text_health = font.render(str(player.health) + '/' + str(HEALTH), 1, COLOR['white'])
        text_protection = font.render(str(player.protection) + '/' + str(PROTECTION), 1, COLOR['white'])
        text_bullets = font.render(str(player.bullets) + '/' + str(BULLETS), 1, COLOR['white'])
        text_coin = font.render(str(player.coins), 1, COLOR['black'])
        self.image = pygame.Surface((160, 80))
        self.image.fill(COLOR['azure'])
        pygame.draw.rect(self.image, COLOR['blue'], (0, 0, 160, 80), 1)

        self.image.blit(load_image('heart.png', -1), (5, 5))
        pygame.draw.rect(self.image, COLOR['black'], (34, 4, 122, 22))
        pygame.draw.rect(self.image, (COLOR['red']), (35, 5, ceil(120 * player.health / HEALTH), 20))

        self.image.blit(load_image('shild.png', -1), (5, 30))
        pygame.draw.rect(self.image, COLOR['black'], (34, 29, 122, 22))
        pygame.draw.rect(self.image, COLOR['orange'], (35, 30, ceil(120 * player.protection / PROTECTION), 20))

        self.image.blit(load_image('bullets.png', -1), (5, 55))
        pygame.draw.rect(self.image, COLOR['black'], (34, 54, 72, 22))
        pygame.draw.rect(self.image, COLOR['magenta'], (35, 55, ceil(70 * player.bullets / BULLETS), 20))

        self.image.blit(load_image('coins.png', -1), (110, 55))

        self.image.blit(text_health, (95 - text_health.get_width() // 2, 9))
        self.image.blit(text_protection, (95 - text_protection.get_width() // 2, 34))
        self.image.blit(text_bullets, (70 - text_bullets.get_width() // 2, 59))
        self.image.blit(text_coin, (132, 59))


class Projectile(pygame.sprite.Sprite):
    # 炮弹激光级
    def __init__(self, type_of_projectile, initial_coords, final_coords, color, damage):
        super().__init__(all_sprites)
        self.damage = damage
        self.type_of_projectile = type_of_projectile
        self.initial_coords = initial_coords
        self.final_coords = final_coords
        if type_of_projectile == 'laser':
            self.c = 0
            self.proof_for_damage = True
            self.color = COLOR[color]
            if abs(self.initial_coords[0] - self.final_coords[0]) > abs(self.initial_coords[1] - self.final_coords[1]):
                self.initial_width = laser_max_size * tile_height
                self.initial_height = max(self.initial_width * abs(self.initial_coords[1] - self.final_coords[1]) /
                                          abs(self.initial_coords[0] - self.final_coords[0]), 3)
            else:
                self.initial_height = laser_max_size * tile_width
                self.initial_width = max(3, self.initial_height * abs(self.initial_coords[0] - self.final_coords[0]) /
                                         abs(self.initial_coords[1] - self.final_coords[1]))
            self.image = pygame.Surface((self.initial_width, self.initial_height))
            self.image.set_colorkey(self.image.get_at((0, 0)))
            if self.initial_coords[0] >= self.final_coords[0] and self.initial_coords[1] >= self.final_coords[1]:
                pygame.draw.line(self.image, self.color, (0, 0), (self.initial_width - 1, self.initial_height - 1), 3)
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.bottomright = self.initial_coords
                self.coords = list()
                for sprite in walls_group:
                    if pygame.sprite.collide_mask(self, sprite):
                        self.coords.append(pygame.sprite.collide_mask(self, sprite))
                self.nearest_coord = max(self.coords)[0], max(self.coords, key=lambda x: x[1])[1]
                self.width = max(3, self.initial_width - self.nearest_coord[0])
                self.height = max(3, self.initial_height - self.nearest_coord[1])
                self.image = pygame.Surface((self.width, self.height))
                self.image.set_colorkey(self.image.get_at((0, 0)))
                pygame.draw.line(self.image, self.color, (0, 0), (self.width - 1, self.height - 1), 3)
                self.rect = self.image.get_rect()
                self.rect.bottomright = self.initial_coords
            elif self.initial_coords[0] <= self.final_coords[0] and self.initial_coords[1] <= self.final_coords[1]:
                pygame.draw.line(self.image, self.color, (0, 0), (self.initial_width - 1, self.initial_height - 1), 3)
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.topleft = self.initial_coords
                self.coords = list()
                for sprite in walls_group:
                    if pygame.sprite.collide_mask(self, sprite):
                        self.coords.append(pygame.sprite.collide_mask(self, sprite))
                self.nearest_coord = min(self.coords)[0], min(self.coords, key=lambda x: x[1])[1]
                self.width = max(3, self.nearest_coord[0])
                self.height = max(3, self.nearest_coord[1])
                self.image = pygame.Surface((self.width, self.height))
                self.image.set_colorkey(self.image.get_at((0, 0)))
                pygame.draw.line(self.image, self.color, (0, 0), (self.width - 1, self.height - 1), 3)
                self.rect = self.image.get_rect()
                self.rect.topleft = self.initial_coords
            elif self.initial_coords[0] >= self.final_coords[0] and self.initial_coords[1] <= self.final_coords[1]:
                pygame.draw.line(self.image, self.color, (0, self.initial_height - 1), (self.initial_width - 1, 0), 3)
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.topright = self.initial_coords
                self.coords = list()
                for sprite in walls_group:
                    if pygame.sprite.collide_mask(self, sprite):
                        self.coords.append(pygame.sprite.collide_mask(self, sprite))
                self.nearest_coord = max(self.coords)[0], min(self.coords, key=lambda x: x[1])[1]
                self.width = max(3, self.initial_width - self.nearest_coord[0])
                self.height = max(3, self.nearest_coord[1])
                self.image = pygame.Surface((self.width, self.height))
                self.image.set_colorkey(self.image.get_at((0, 0)))
                pygame.draw.line(self.image, self.color, (0, self.height - 1), (self.width - 1, 0), 3)
                self.rect = self.image.get_rect()
                self.rect.topright = self.initial_coords
            else:
                pygame.draw.line(self.image, self.color, (0, self.initial_height - 1), (self.initial_width - 1, 0), 3)
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.bottomleft = self.initial_coords
                self.coords = list()
                for sprite in walls_group:
                    if pygame.sprite.collide_mask(self, sprite):
                        self.coords.append(pygame.sprite.collide_mask(self, sprite))
                self.nearest_coord = min(self.coords)[0], max(self.coords, key=lambda x: x[1])[1]
                self.width = max(3, self.nearest_coord[0])
                self.height = max(3, self.initial_height - self.nearest_coord[1])
                self.image = pygame.Surface((self.width, self.height))
                self.image.set_colorkey(self.image.get_at((0, 0)))
                pygame.draw.line(self.image, self.color, (0, self.height - 1), (self.width - 1, 0), 3)
                self.rect = self.image.get_rect()
                self.rect.bottomleft = self.initial_coords
        else:
            self.image = load_image('bullet.png')
            self.rect = self.image.get_rect()
            self.rect.center = self.initial_coords
            self.x = 0
            self.y = 0
            self.coefficient_x = abs(self.initial_coords[0] - self.final_coords[0])
            self.coefficient_y = abs(self.initial_coords[1] - self.final_coords[1])
            if self.coefficient_y == self.coefficient_x == 0:
                self.vector = (0, 0)
            elif self.rect.center[0] >= self.final_coords[0] and self.rect.center[1] >= self.final_coords[1]:
                self.unit_vector = 3 / (self.coefficient_x + self.coefficient_y)
                self.vector = (- self.unit_vector * self.coefficient_x, - self.unit_vector * self.coefficient_y)
            elif self.rect.center[0] <= self.final_coords[0] and self.rect.center[1] <= self.final_coords[1]:
                self.unit_vector = 3 / (self.coefficient_x + self.coefficient_y)
                self.vector = (self.unit_vector * self.coefficient_x, self.unit_vector * self.coefficient_y)
            elif self.rect.center[0] <= self.final_coords[0] and self.rect.center[1] >= self.final_coords[1]:
                self.unit_vector = 3 / (self.coefficient_x + self.coefficient_y)
                self.vector = (self.unit_vector * self.coefficient_x, - self.unit_vector * self.coefficient_y)
            elif self.rect.center[0] >= self.final_coords[0] and self.rect.center[1] <= self.final_coords[1]:
                self.unit_vector = 3 / (self.coefficient_x + self.coefficient_y)
                self.vector = (- self.unit_vector * self.coefficient_x, self.unit_vector * self.coefficient_y)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # 该炮弹的发射声和移动声及清除其本身的功能
        if self.type_of_projectile == 'laser':
            if self.c == 0:
                playing_sound("lazer.ogg")
            elif self.c == 1:
                self.proof_for_damage = False
            self.c += 1
            if self.c == 10:
                self.kill()
        else:
            self.rect = self.rect.move(int(self.x + self.vector[0]) - int(self.x),
                                       int(self.y + self.vector[1]) - int(self.y))
            self.x += self.vector[0]
            self.y += self.vector[1]
            if pygame.sprite.spritecollideany(self, walls_group):
                playing_sound("for_gun_1.ogg")
                self.kill()


class Weapon(pygame.sprite.Sprite):
    # 各类武器
    def __init__(self, damage, cost, rate_of_fire, filename, pos_x, pos_y, butt, type_of_projectile, color=None):
        super().__init__(weapons_group, all_sprites)
        self.cost = cost
        self.damage = damage
        self.rate_of_fire = rate_of_fire
        self.image = load_image(filename, -1)
        self.main_image = self.image
        self.main_image1 = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect().move(pos_x * tile_width, pos_y * tile_height)
        self.butt = butt
        self.type_of_projectile = type_of_projectile
        self.color = color

    def update(*args):
        # 武器的选择功能。
        for weap in weapons_group:
            if pygame.sprite.spritecollideany(weap, player_group):
                if len(player.weapons) != 2:
                    player.weapon.remove(hero_weapon_group)
                    hero_weapon_group.add(weap)
                    weap.remove(weapons_group)
                    player.weapons.append(weap)
                    player.number_of_weapon = 1
                    player.weapon = player.weapons[player.number_of_weapon]
                else:
                    weapons_group.add(player.weapon)
                    player.weapon.image = player.weapon.main_image
                    player.weapon.remove(hero_weapon_group)
                    del player.weapons[player.number_of_weapon]
                    player.weapon = weap
                    hero_weapon_group.add(player.weapon)
                    weap.remove(weapons_group)
                    player.weapons.insert(player.number_of_weapon, weap)

    def change(*args):
        # 武器转换函数
        if len(player.weapons) == 2:
            if player.number_of_weapon == 0:
                player.weapon.remove(hero_weapon_group)
                player.weapon = player.weapons[1]
                hero_weapon_group.add(player.weapon)
                player.number_of_weapon = 1
            elif player.number_of_weapon == 1:
                player.weapon.remove(hero_weapon_group)
                player.weapon = player.weapons[0]
                hero_weapon_group.add(player.weapon)
                player.number_of_weapon = 0


class Potion(pygame.sprite.Sprite):
    # 药剂类
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(potion_group, all_sprites)
        if tile_type == "health1":
            self.health_potion = HEALTH_POTION1
            self.bullets_potion = 0
        elif tile_type == "bullet1":
            self.health_potion = 0
            self.bullets_potion = BULLET_POTION1
        self.image = potion_images[tile_type]
        potion_group.add(self)
        self.rect = self.image.get_rect().move(tile_width * pos_x + 10, tile_height * pos_y + 10)

    def update(*args):
        # 药水作用
        for pot in potion_group:
            if pygame.sprite.spritecollideany(pot, player_group):
                player.health += pot.health_potion
                if player.health > HEALTH:
                    player.health = HEALTH
                player.bullets += pot.bullets_potion
                if player.bullets > BULLETS:
                    player.bullets = BULLETS
                pot.kill()


class Enemy(pygame.sprite.Sprite):
    # 一群像英雄一样的对手。
    def __init__(self, health, pos_x, pos_y, filename, weapon, animation, animation1, death, brake):
        super().__init__(enemy_group, all_sprites)
        self.f = True
        self.imagedeath = load_image(death, -1)
        self.brake = brake
        self.image1 = load_image(filename, -1)
        self.image2 = pygame.transform.flip(self.image1, True, False)
        self.image = self.image1
        self.animation2 = (load_image(animation, -1), load_image(animation1, -1))
        self.animation1 = (pygame.transform.flip(load_image(animation, -1), True, False),
                           pygame.transform.flip(load_image(animation1, -1), True, False))
        self.health = health
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x * tile_width, pos_y * tile_height)
        self.weapon = weapon
        enemy_weapon_group.add(self.weapon)
        self.weapon.remove(weapons_group)
        self.k = randint(0, 4 * FPS - 1)
        self.c = 0
        self.regulator = 0

    def update(self):
        # 敌人武器扭转函数
        if self.health > 0:
            if player.rect.center[0] > self.rect.x + 15:
                self.weapon.rect.topleft = (self.rect.x + WEAPON_X - self.weapon.butt, self.rect.y + WEAPON_Y)
                x_distance = player.rect.center[0] - self.weapon.rect.x
                if -2 <= x_distance <= 2:
                    if player.rect.center[1] <= self.rect.center[1]:
                        angle = 90
                    else:
                        angle = -90
                else:
                    angle = degrees(atan((self.weapon.rect.y - player.rect.center[1]) / x_distance))
                    angle = degrees(atan((self.weapon.rect.y - (self.weapon.rect.h - self.weapon.rect.w) * sin(
                        radians(angle)) - player.rect.center[1]) / x_distance))
                self.weapon.image = pygame.transform.rotate(self.weapon.main_image, angle)
                if player.rect.center[1] < self.weapon.rect.y:
                    self.weapon.rect = self.weapon.rect.move(0, (self.weapon.rect.h - self.weapon.rect.w) * sin(
                        radians(angle)))
            else:
                self.weapon.rect.topright = (self.rect.x - WEAPON_X + self.weapon.butt + self.rect.w,
                                              self.rect.y + WEAPON_Y)
                x_distance = player.rect.center[0] - self.weapon.rect.topright[0]
                if -2 <= x_distance <= 2:
                    if player.rect.center[1] >= self.rect.center[1]:
                        angle = 90
                    else:
                        angle = -90
                else:
                    angle = degrees(atan((self.weapon.rect.y - player.rect.center[1]) / x_distance))
                    angle = degrees(atan((self.weapon.rect.y - (self.weapon.rect.h - self.weapon.rect.w) * sin(
                        radians(angle)) - player.rect.center[1]) / x_distance))
                self.weapon.image = pygame.transform.rotate(self.weapon.main_image1, angle)
                if player.rect.center[1] < self.weapon.rect.y:
                    self.weapon.rect = self.weapon.rect.move(0, (self.weapon.rect.w - self.weapon.rect.h) * sin(
                        radians(angle)))
                    self.weapon.rect = self.weapon.rect.move(
                        -(self.weapon.rect.w - self.weapon.rect.h) * sin(radians(angle)), 0)
                else:
                    self.weapon.rect = self.weapon.rect.move(
                        (self.weapon.rect.w - self.weapon.rect.h) * sin(radians(angle)), 0)
            for projectile in hero_projectile:
                if pygame.sprite.collide_mask(self, projectile):
                    if projectile.type_of_projectile == 'bullet':
                        self.regenerator = -1
                        self.regulator = -1
                        self.health = max(0, self.health - projectile.damage)
                        playing_sound("for_gun_1.ogg")
                        projectile.kill()
                    elif projectile.proof_for_damage:
                        self.health = max(0, self.health - projectile.damage)
        else:
            if self.f:
                player.coins += 2
                player.bullets = min(BULLETS, player.bullets + 6)
                self.weapon.image = self.weapon.main_image
                create_particles(20, self.rect.center)
                weapons_group.add(self.weapon)
                self.weapon.remove(enemy_weapon_group)
                self.rect = self.rect.move(0, self.rect.height - self.imagedeath.get_rect().height)
                self.image = self.imagedeath
                self.f = False

    def go(self):
        # 敌人的移动和动画功能
        if self.regulator == 0:
            if player.rect.center[0] > self.rect.center[0]:
                self.rect.x += 1
                if pygame.sprite.spritecollideany(self, walls_group):
                    self.rect.x -= 1
            elif player.rect.center[0] < self.rect.center[0]:
                self.rect.x -= 1
                if pygame.sprite.spritecollideany(self, walls_group):
                    self.rect.x += 1
            if player.rect.center[1] > self.rect.center[1]:
                self.rect.y += 1
                if pygame.sprite.spritecollideany(self, walls_group):
                    self.rect.y -= 1
            elif player.rect.center[1] < self.rect.center[1]:
                self.rect.y -= 1
                if pygame.sprite.spritecollideany(self, walls_group):
                    self.rect.y += 1
            if self.c < 25:
                if player.rect.center[0] > self.rect.center[0]:
                    self.image = self.animation2[0]
                else:
                    self.image = self.animation1[0]
            elif self.c < 50:
                if player.rect.center[0] > self.rect.center[0]:
                    self.image = self.animation2[1]
                else:
                    self.image = self.animation1[1]
        self.regulator = (self.regulator + 1) % self.brake
        if self.c == 50:
            self.c = -1
        self.c += 1

    def stop(self):
        # 敌人停止功能
        self.c = 0
        if self.rect.center[0] >= player.rect.center[0]:
            self.image = self.image2
        else:
            self.image = self.image1

    def shot(self):
        # 敌人射击函数
        enemy_projectile.add(Projectile(self.weapon.type_of_projectile, self.weapon.rect.center, player.rect.center,
                                        self.weapon.color, self.weapon.damage))

    def behavior(self):
        # 敌人行为函数
        if self.health > 0:
            if self.k < 2 * FPS:
                self.go()
            elif 2 * FPS <= self.k < 4 * FPS:
                self.stop()
            else:
                self.shot()
            self.k = (self.k + 1) % (4 * FPS + 1)
        else:
            self.death()

    def death(self):
        pass


class Boss(Enemy):
    # 改善对手
    def __init__(self, health, pos_x, pos_y, filename, weapon, animation, animation1, death, brake):
        super().__init__(health, pos_x, pos_y, filename, weapon, animation, animation1, death, brake)
        self.regulator = 0
        self.k = randint(0, 3 * FPS - 1)

    def behavior(self):
        # 敌人行为函数
        if self.health > 0:
            if self.k < 2 * FPS:
                self.go()
            elif 2 * FPS <= self.k < 3 * FPS:
                self.stop()
            else:
                self.shot()
            self.k = (self.k + 1) % (3 * FPS + 1)
        else:
            self.death()


class Particle(pygame.sprite.Sprite):
    # 阶级粒子
    def __init__(self, coords):
        super().__init__(all_sprites, particle_group)
        self.vector = (randint(-3, 3), randint(-3, 3))
        self.image = particle_images[randint(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.c = 0

    def update(self):
        # 粒子运动和清除函数
        self.rect = self.rect.move(self.vector)
        if self.c == 10:
            self.kill()
        self.c += 1


# 建立彩旗
move_map = False
open_start_screen = True
proof_for_song = True
proof_for_sound = True
open_finish_screen = False
FPS = 200
pygame.init()
WIDTH = 500
HEIGHT = 500
WEAPON_X = 18
WEAPON_Y = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color('black'))
# 基本图像和其他必要常数
COLOR = {'black': pygame.Color('black'), 'white': pygame.Color('white'), 'red': pygame.Color('red'),
         'green': pygame.Color('green'), 'blue': pygame.Color('blue'), 'yellow': pygame.Color('yellow'),
         'cyan': pygame.Color('cyan'), 'magenta': pygame.Color('magenta'), 'azure': (150, 255, 255),
         'orange': pygame.Color('orange')}

tile_images = {'wall': load_image('wall.png'), 'empty': load_image('flour.png'),
               "portal": load_image('portal.png', -1),
               'd_wall': load_image('d_wall.png'), 'wall1': load_image('d_wall.png')}
potion_images = {"health1": load_image('health1.png', -1), "bullet1": load_image('bullet1.png', -1)}
player_image = load_image('hero.png', -1)
player_animation = (load_image('heromove1.png', -1), load_image('heromove2.png', -1))
player_image1 = pygame.transform.flip(load_image('hero.png', -1), True, False)
player_animation1 = (pygame.transform.flip(load_image('heromove1.png', -1), True, False),
                     pygame.transform.flip(load_image('heromove2.png', -1), True, False))
player_death = load_image('herodeath.png', -1)
image_sound_on = load_image('volume_on.png')
image_sound_off = load_image('volume_off.png')
image_song_on = load_image('song_on.png')
image_song_off = load_image('song_off.png')
particle_images = [load_image('bullet2.png', -1), load_image('hearth.png', -1), load_image('coin.png', -1)]
tile_width = 32
tile_height = 32
clock = pygame.time.Clock()
HEALTH = 5
PROTECTION = 5
BULLETS = 200
HEALTH_POTION1 = 1
HEALTH_POTION2 = 2
HEALTH_POTION3 = 4
BULLET_POTION1 = 30
BULLET_POTION2 = 60
BULLET_POTION3 = 120
next_level = True
delete = False


def game():
    # 发射功能
    global player, potion_group, weapons_group, hero_weapon_group, hero_projectile, enemy_group, \
        enemy_projectile, hwalls_group, walls_group, all_sprites, enemy_weapon_group, tiles_group, player_group, colt,\
        proof_for_song, proof_for_sound, running, enemy, enemy1, enemy2, h, d, l, r, screen, clock, open_start_screen,\
        move_map, colt, portal_group, open_finish_screen, particle_group, next_level, delete, PLAYER_HEALTH, \
        PLAYER_HEALTH, PLAYER_BULLETS, PLAYER_PROTECTION, PLAYER_REGULATOR, PLAYER_REGENERATOR, PLAYER_C, \
        PLAYER_WEAPONS, PLAYER_NUMBER_OF_WEAPON

    if next_level and move_map:
        PLAYER_HEALTH = player.health
        PLAYER_BULLETS = player.bullets
        PLAYER_PROTECTION = player.protection
        PLAYER_REGULATOR = player.regulator
        PLAYER_REGENERATOR = player.regenerator
        PLAYER_WEAPONS = player.weapons
        PLAYER_NUMBER_OF_WEAPON = player.number_of_weapon
        PLAYER_C = player.c
        next_level = False
    if delete:
        for sprite in all_sprites:
            sprite.kill()
    else:
        delete = True
    particle_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    potion_group = pygame.sprite.Group()
    weapons_group = pygame.sprite.Group()
    hero_weapon_group = pygame.sprite.GroupSingle()
    hero_projectile = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_projectile = pygame.sprite.Group()
    hwalls_group = pygame.sprite.Group()
    walls_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    enemy_weapon_group = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    if move_map:
        colt = Weapon(2, 0, 1, 'colt.png', 1, 1, 0, 'bullet')
        player = generate_level(load_level('map2.txt'))
        player.coins = 24
        player.health = PLAYER_HEALTH
        player.protection = PLAYER_PROTECTION
        player.bullets = PLAYER_BULLETS
        player.c = PLAYER_C
        player.regenerator = PLAYER_REGENERATOR
        player.regulator = PLAYER_REGULATOR
        player.weapons = PLAYER_WEAPONS
        player.number_of_weapon = PLAYER_NUMBER_OF_WEAPON
        colt.kill()
        player.weapon = PLAYER_WEAPONS[player.number_of_weapon]
        for sprite in PLAYER_WEAPONS:
            all_sprites.add(sprite)
        hero_weapon_group.add(player.weapon)
        Weapon(6, 2, 3, 'b_blaster.png', 7, 19, 4, 'laser', 'blue')
        Potion('health1', 23, 5)
        Potion('health1', 4, 16)
        Potion('health1', 4, 21)
        Enemy(20, 33, 18, 'enemy1.png', Weapon(3, 0, 1, 'colt2.png', 21, 8, 0, 'bullet'),
              'enemy1m1.png', 'enemy1m2.png', 'enemy1d.png', 3)
        Enemy(20, 25, 18, 'enemy1.png', Weapon(3, 0, 1, 'colt2.png', 21, 8, 0, 'bullet'),
              'enemy1m1.png', 'enemy1m2.png', 'enemy1d.png', 3)
        Enemy(20, 22, 8, 'enemy1.png', Weapon(3, 0, 1, 'colt2.png', 21, 8, 0, 'bullet'),
              'enemy1m1.png', 'enemy1m2.png', 'enemy1d.png', 3)
        Enemy(20, 24, 8, 'enemy1.png', Weapon(3, 0, 1, 'colt2.png', 21, 8, 0, 'bullet'),
              'enemy1m1.png', 'enemy1m2.png', 'enemy1d.png', 3)
        Enemy(20, 29, 14, 'enemy1.png', Weapon(3, 0, 1, 'colt2.png', 21, 8, 0, 'bullet'),
              'enemy1m1.png', 'enemy1m2.png', 'enemy1d.png', 3)
        Enemy(20, 22, 12, 'enemy1.png', Weapon(3, 0, 1, 'colt2.png', 21, 8, 0, 'bullet'),
              'enemy1m1.png', 'enemy1m2.png', 'enemy1d.png', 3)
        Enemy(20, 23, 15, 'enemy1.png', Weapon(3, 0, 1, 'colt2.png', 21, 8, 0, 'bullet'),
              'enemy1m1.png', 'enemy1m2.png', 'enemy1d.png', 3)
        Enemy(20, 25, 15, 'enemy1.png', Weapon(3, 0, 1, 'colt2.png', 21, 8, 0, 'bullet'),
              'enemy1m1.png', 'enemy1m2.png', 'enemy1d.png', 3)
        Boss(150, 57, 7, 'boss.png', Weapon(4, 2, 1, 'g_blaster.png', 57, 7, 4, 'laser', 'green'),
             'bossm1.png', 'bossm2.png', 'bossd.png', 3)
    else:
        colt = Weapon(2, 0, 1, 'colt.png', 1, 1, 0, 'bullet')
        Weapon(3, 1, 5, 'gun.png', 40, 23, 4, 'bullet')
        hero_weapon_group.add(colt)
        colt.remove(weapons_group)
        player, level_x, level_y = generate_level(load_level('map.txt'))
        Enemy(10, 12, 27, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 8, 25, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 12, 21, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 6, 29, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 4, 26, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 1, 21, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Potion('health1', 43, 20)
        Potion('bullet1', 35, 20)
        Potion('health1', 25, 57)
        Potion('bullet1', 25, 48)
        Weapon(20, 6, 1, 'rifle.png', 30, 55, 4, 'bullet')
        Enemy(10, 1, 41, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 12, 41, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 4, 44, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 12, 47, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 5, 49, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
        Enemy(10, 1, 52, 'enemy2.png', Weapon(2, 0, 1, 'colt3.png', 1, 1, 0, 'bullet'),
              'enemy2m1.png', 'enemy2m2.png', 'enemy2d.png', 3)
    h = False
    d = False
    l = False
    r = False
    if open_finish_screen:
        finish_screen()
    if open_start_screen:
        start_screen()
    camera = Camera()
    fire = False
    if proof_for_song:
        playing_song("song1.ogg")
    running = True
    while running:
        event = None
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
                elif event.key == pygame.K_a:
                    l = True
                elif event.key == pygame.K_w:
                    h = True
                elif event.key == pygame.K_s:
                    d = True
                elif event.key == pygame.K_d:
                    r = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    l = False
                elif event.key == pygame.K_w:
                    h = False
                elif event.key == pygame.K_s:
                    d = False
                elif event.key == pygame.K_d:
                    r = False
                if event.key == pygame.K_f:
                    Potion.update()
                    Weapon.update()
                if event.key == pygame.K_SPACE:
                    player.portal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.health > 0:
                    if event.button == 4 or event.button == 5:
                        Weapon.change()
                if event.button == 1:
                    if 160 < pygame.mouse.get_pos()[0] < 200 and HEIGHT - 40 <= pygame.mouse.get_pos()[1] <= HEIGHT:
                        if proof_for_song:
                            pygame.mixer.music.pause()
                            proof_for_song = False
                        else:
                            pygame.mixer.music.unpause()
                            proof_for_song = True
                    elif 160 < pygame.mouse.get_pos()[0] < 200 \
                            and HEIGHT - 80 <= pygame.mouse.get_pos()[1] < HEIGHT - 40:
                        if proof_for_sound:
                            proof_for_sound = False
                        else:
                            proof_for_sound = True
                    elif pygame.mouse.get_pos()[0] >= 200 or HEIGHT - 80 > pygame.mouse.get_pos()[1]:
                        fire = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and not (pygame.mouse.get_pos()[0] < 50 and pygame.mouse.get_pos()[1] < 50):
                    fire = False
        if fire:
            player.shot()
        hero_projectile.update()
        for sprite in enemy_group:
            sprite.behavior()
            sprite.update()
        particle_group.update()
        enemy_projectile.update()
        player.update()
        player.animation()
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        tiles_group.draw(screen)
        potion_group.draw(screen)
        walls_group.draw(screen)
        weapons_group.draw(screen)
        enemy_group.draw(screen)
        enemy_projectile.draw(screen)
        enemy_weapon_group.draw(screen)
        portal_group.draw(screen)
        player_group.draw(screen)
        hero_projectile.draw(screen)
        hero_weapon_group.draw(screen)
        particle_group.draw(screen)
        hwalls_group.draw(screen)
        screen.blit(Panel().image, (0, 0))
        clock.tick(FPS)
        if proof_for_song:
            screen.blit(image_song_on, (160, HEIGHT - 40))
        else:
            screen.blit(image_song_off, (160, HEIGHT - 40))
        if proof_for_sound:
            screen.blit(image_sound_on, (160, HEIGHT - 80))
        else:
            screen.blit(image_sound_off, (160, HEIGHT - 80))
        pygame.display.flip()
    if not running:
        game()


game()
