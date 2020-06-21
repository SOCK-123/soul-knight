# _*_ coding: utf-8 _*_
from src.character import *
import pygame
import os
def load_image(name, colorkey=None):
    # 图像加载功能
    fullname = os.path.join('../data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
def load_map(filename):
    # 打开文本功能
    filename = "../data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]
    max_width = max(map(len, level_map))
    level_map = list(map(lambda x: x.ljust(max_width, " "), level_map))
    return level_map
def generate_level(level, px, py):
    # 创建地图,精灵的函数
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y, px, py)
            elif level[y][x] == '#':
                Tile('d_wall', x, y + 0.5, px, py)
            elif level[y][x] == '@':
                Tile('empty', x, y, px, py)

    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Tile('wall', x, y, px, py)
            elif level[y][x] == '%':
                Tile('portal', x, y, px, py)
def choss(mapnum,map,hero0):
    if (mapnum == 0):
        if map.maplist[hero0.heroy // 100 - 1][hero0.herox // 100 - 2] == '%' and 750 < hero0.herox < 1150:
            return 1
        elif map.maplist[hero0.heroy // 100 - 1][hero0.herox // 100 - 2] == '%' and 3950 < hero0.herox < 4350:
            return 2
        elif map.maplist[hero0.heroy // 100 - 1][hero0.herox // 100 - 2] == '%' and 3900 < hero0.herox < 4400:
            return 3
        elif map.maplist[hero0.heroy // 100 - 1][hero0.herox // 100 - 2] == '%' and 200 < hero0.herox < 500:
            return 99
    if map.maplist[hero0.heroy // 100 - 1][hero0.herox // 100 - 2] == '%':
        if (mapnum != map.mapnunm_max):
            return mapnum+1
    return False
class Map:
    def __init__(self,x,y,mapnum,maplist):
        self.mapnum=mapnum
        self.maplist=maplist
        self.mapnunm_max = 3
        self.map_height = 100 * len(self.maplist)
        self.map_width = 100 * len(self.maplist[0])
        screen.fill(pygame.Color('black'))
        generate_level(self.maplist,x,y)
class Judge:
    def __init__(self,x,y,maplist=load_map('map1.txt')):
        self.x=x-100
        self.y=y
        self.maplist=maplist
    def up(self):
        if(self.maplist[(self.y-7)//100][self.x//100] !='#' ):
            return True
        return False
    def down(self):
        if (self.maplist[(self.y+7+50)//100][self.x//100] != '#'):
            return True
        return False
    def left(self):
        if (self.maplist[self.y//100][(self.x-7)//100] != '#'):
            return True
        return False
    def right(self):
        if (self.maplist[self.y//100][(self.x+7+20)//100] != '#'):
            return True
        return False
class Tile(pygame.sprite.Sprite):
    # 墙壁和地板的类，地图，静态的东西。
    def __init__(self, tile_type, pos_x, pos_y,x,y):
        self.image = images[tile_type]
        roll=Roll(x,y)
        if tile_type == 'd_wal1':
            self.rect =(tile_width * pos_x+roll.x, tile_height * pos_y+roll.y)
        elif tile_type == 'wall':
            self.rect =(tile_width * pos_x+roll.x, tile_height * pos_y - 16+roll.y)
        elif tile_type == 'portal':
            self.rect = (tile_width* pos_x + roll.x, tile_height * pos_y + roll.y)
        else:
            self.rect =(tile_width * pos_x+roll.x, tile_height * pos_y+roll.y)
        screen.blit(self.image, self.rect)
class Roll:
    global map_width,map_height
    def __init__(self,role_x, role_y, WIN_WIDTH=1080, WIN_HEIGHT=720):
        self.x = -(role_x - WIN_WIDTH / 2)
        self.y = -(role_y - WIN_HEIGHT / 2)
windows_size = (1080, 720)
tile_width = 100
tile_height =100



screen = pygame.display.set_mode(windows_size)      # 启动屏幕
# 加载图片并转换
images = {'wall': load_image('wall.png'), 'empty': load_image('flour.png'), 'd_wall': load_image('d_wall.png'),'portal':load_image('portal.png')}


