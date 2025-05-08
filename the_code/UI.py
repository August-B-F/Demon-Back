import pygame
import sys 
import os
import time as t
import math
import threading

from the_code.constants import *
from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def main_menu():
 
    menu=True
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN:
                    menu=False
 
        start = pygame.image.load(os.path.join(game_folder, 'img/sener/STARTBILD_V2.png')).convert()
        start = pygame.transform.scale(start, (WIDTH, HEIGHT))
        pos = start.get_rect()
        pos.centerx = WIN.get_rect().centerx 
        WIN.blit(start, pos)

        title= text_format("DemonBack", font, 45, WHITE)
        text_start= text_format("press any button", font, 20, RED)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
 
        WIN.blit(title, (WIDTH/2 - (title_rect[2]/2), 30))
        WIN.blit(text_start, (WIDTH/2 - (start_rect[2]/2), 500))
        pygame.display.update()
        CLOCK.tick(FPS)