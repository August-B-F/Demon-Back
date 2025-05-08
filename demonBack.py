import time as t
import pygame   
import os

from the_code.levels import *
from the_code.assetc import *
from the_code.constants import *
from the_code.spelare import *
from the_code.UI import *

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

pygame.init()

levelbild('img/sener/intro_v2.png')
pygame.display.set_caption('Demon Back')  
pygame.display.update()
t.sleep(2)
main_menu()
healing.play()
redfade(WIDTH, HEIGHT)
pygame.display.update()

running = True

key = pygame.key.get_pressed()

cave.play(-1)

while running:

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

  the_game.state_manager()
  
  if player_health.current_health < 1: 
    all_sprites.clear(WIN, background)
    levelbild('img/sener/game over_v2.png')
    pygame.display.update()
    t.sleep(2)
    pygame.quit()
    sys.exit()
    
  pygame.display.flip()
  CLOCK.tick(FPS) 

pygame.quit()