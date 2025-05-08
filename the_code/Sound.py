import pygame
import sys 
import os
import time as t
import math
import threading

from pygame.time import Clock

pygame.init()

victory = pygame.mixer.Sound('the_code/sounds/victory.wav')
cave = pygame.mixer.Sound('the_code/sounds/cave.wav')
sword = pygame.mixer.Sound('the_code/sounds/sword_v2.wav')
forest = pygame.mixer.Sound('the_code/sounds/forest.wav')
healing = pygame.mixer.Sound('the_code/sounds/healing.wav')
dark_forest = pygame.mixer.Sound('the_code/sounds/dark_forest.wav')
dark_forest.set_volume(0.5)
cave.set_volume(0.5)
healing.set_volume(0.3)