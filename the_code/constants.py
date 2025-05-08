import pygame
import sys 
import os
import time as t
import math
import threading

from pygame.time import Clock

WIDTH = 900
HEIGHT = 600

os.environ['SDL_VIDEO_CENTERED'] = '1'
font = "the_code/fonts/prstart.ttf"

FPS = 60
CLOCK = pygame.time.Clock() 

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE + pygame.SCALED)
background = pygame.Surface(WIN.get_size())

#färger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# olika enemys, namn häla exp, etc. 
monster_data = {
	'gobline': {'health': 100,'img': 'img/mobs/goblin.png','damage':20, 'speed': 2, 'resistance': 20},
	'magiGobline': {'health': 100,'img': 'img/mobs/goblin.png','damage':40, 'speed': 2, 'resistance': 20},
	'goblineKing': {'health': 300,'img': 'img/mobs/goblin king_v2.png','damage':80, 'speed': 2, 'resistance': 10}}

player_stats = {
    'health': 200,'attack': 25,'speed': 4, 'dogespeed': 10}

################################################ NPC ani ###########################################################
NPC_ani = [pygame.image.load("the_code/img/NPC/frog1.png"), pygame.image.load("the_code/img/NPC/frog2.png"),
           pygame.image.load("the_code/img/NPC/frog1.png"), pygame.image.load("the_code/img/NPC/frog2.png"),
           pygame.image.load("the_code/img/NPC/frog2.png")]

enemy_death_ani = [pygame.image.load("the_code/img/smoke2/0.png"), pygame.image.load("the_code/img/smoke2/1.png"),
           pygame.image.load("the_code/img/smoke2/2.png"), pygame.image.load("the_code/img/smoke2/3.png"),
           pygame.image.load("the_code/img/smoke2/4.png"), pygame.image.load("the_code/img/smoke2/5.png")]

def levelbild(bild):
    startscreen_image = pygame.image.load(os.path.join(game_folder, bild)).convert()
    startscreen_image = pygame.transform.scale(startscreen_image, (WIDTH, HEIGHT))
    startscreen_rect = startscreen_image.get_rect()
    x = (WIDTH/2) - (startscreen_rect.width /2)
    y = (HEIGHT/2) - (startscreen_rect.height /2)
    WIN.blit(startscreen_image, (x,y))



