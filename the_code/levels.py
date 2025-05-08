import pygame
import sys 
import os
import time as t
import math
import threading

from the_code.assetc import * 
from the_code.constants import *
from the_code.enemy import *
from the_code.spelare import * 
from the_code.Sound import * 

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

En1_5 = Enemy('gobline',300,300,enemys_level5,30,40,'En1_5')
En2_5 = Enemy('gobline',330,350,enemys_level5,30,40,'En2_5')
En3_5 = Enemy('gobline',500,320,enemys_level5,30,40,'En1_5')
En4_5 = Enemy('gobline',430,250,enemys_level5,30,40,'En2_5')

EnBoss_7 = Enemy('goblineKing',450,200,enemys_level7,120,144,'EnBoss_7')
enemys_all.add(En1_5, En2_5, En3_5, En4_5, EnBoss_7)

class the_Game():

 def __init__(self):
    self.state = 'intro'
    self.alpha = 255
    self.proside = False 
    self.n = 2

 def intro(self):
   all_sprites.update()
   #testbild()
   levelbild('img/levels/level1_v3.png')
   all_sprites.draw(WIN)

   level1_till.draw(WIN)

   mr_f.image.set_alpha(self.alpha)
   if self.alpha > 0:
    self.alpha -= 4
   
   if self.alpha > 0 and self.alpha < 10:
    all_sprites.add(keys,shift,space)

   Hp.update()
   Hp.draw(WIN)

   if player.hitbox.colliderect(m2) and keys not in all_sprites and space not in all_sprites and shift not in all_sprites:
      self.state = 'Level_2'
      self.alpha = 0 
      mr_f.image.set_alpha(self.alpha)
      player.hitbox.center = (480, 100)
      fade(WIDTH, HEIGHT)
      wall_list.empty()
      cave.stop()
      forest.play(-1)
      wall_list.add(Ob_1_2,Ob_2_2,ob_3_2,Ob_4_2,Ob_5_2,ob_6_2,Ob_7_2,Ob_8_2)
    
 def Level_2(self):

    all_sprites.update()
 
    levelbild('img/levels/LEVEL2_TEST2.png')

    all_sprites.draw(WIN)

    Hp.update()
    Hp.draw(WIN)

    if player.hitbox.centery > 570:
       self.state = 'Level_3'
       player.hitbox.center = (760, 30)
       fade(WIDTH, HEIGHT)
       wall_list.empty() 
       wall_list.add(Ob_1_3,Ob_2_3,Ob_3_3,Ob_4_3,Ob_5_3,Ob_6_3,Ob_7_3,Ob_8_3,Ob_9_3,Ob_10_3,Ob_11_3)
       fish.add(Fing)

 def Level_3(self):

    m2.rect.center = (760, 600)

    if player.hitbox.centery < 30:  
       self.state = 'Level_2'
       player.hitbox.center = (450, 560)
       fade(WIDTH, HEIGHT)
       wall_list.empty()
       wall_list.add(Ob_1_2,Ob_2_2,ob_3_2,Ob_4_2,Ob_5_2,ob_6_2,Ob_7_2,Ob_8_2)
       Fing.kill()

    if player.hitbox.colliderect(door): 
       wall_list.empty()
       self.state = 'frogHouse' 
       player.hitbox.center = (450, 355) 
       forest.stop()
       Fing.kill()

       fade(WIDTH, HEIGHT)
       wall_list.add(Ob_1_frog,Ob_2_frog,ob_3_frog,Ob_4_frog,Ob_5_frog,ob_6_frog,Ob_7_frog,Ob_8_frog)
       all_sprites.update()
       all_sprites.draw(WIN)
      
    
    if player.hitbox.colliderect(frog): 
       tillfrog.kill()
       chestB.add(frog_test)
       self.proside = True
    else:
       frog_test.kill()

    if player.hitbox.colliderect(m2) and self.proside:
       self.state = 'Level_4'
       forest.stop()
       fade(WIDTH, HEIGHT)
       dark_forest.play(-1)
       wall_list.empty() 
       wall_list.add(Ob_1_4,Ob_2_4)
       player.hitbox.center = (480, 50)
       Fing.kill()

    all_sprites.update()

    levelbild('img/levels/LEVEL3_TEST3.png')

    mobs.update()
    mobs.draw(WIN)

    chestB.update()
    chestB.draw(WIN)

    fish.update()
    fish.draw(WIN)

    all_sprites.draw(WIN)
    dooren.draw(WIN)

    Hp.update()
    Hp.draw(WIN)

 def frogHouse(self):
  
    if player.hitbox.colliderect(till):
      wall_list.empty()
      self.state = 'Level_3'
      player.hitbox.center = (235, 220) 
      player.update()
      fade(WIDTH, HEIGHT)
      forest.play(-1)
      wall_list.add(Ob_1_3,Ob_2_3,Ob_3_3,Ob_4_3,Ob_5_3,Ob_6_3,Ob_7_3,Ob_8_3,Ob_9_3,Ob_10_3,Ob_11_3)
      all_sprites.update()
      all_sprites.draw(WIN)
      fish.add(Fing)

    all_sprites.update()

    levelbild('img/levels/house4.png')

    all_sprites.draw(WIN)

    tillbaka.update()
    tillbaka.draw(WIN)

    Hp.update()
    Hp.draw(WIN)

 def Level_4(self):

    all_sprites.update()

    levelbild('img/levels/level4_test.png')
    
    all_sprites.draw(WIN)

    Hp.update()
    Hp.draw(WIN)

    est.update()
    est.draw(WIN)

    if player.hitbox.centery < 30:
       self.state = 'Level_3'
       player.hitbox.center = (760, 545)
       dark_forest.stop()
       fade(WIDTH, HEIGHT)
       forest.play(-1)
       wall_list.empty()
       wall_list.add(Ob_1_3,Ob_2_3,Ob_3_3,Ob_4_3,Ob_5_3,Ob_6_3,Ob_7_3,Ob_8_3,Ob_9_3,Ob_10_3,Ob_11_3)
       fish.add(Fing)

    if player.hitbox.centery > 590:
       self.state = 'Level_5'
       wall_list.empty()
       wall_list.add(Ob_1_5,Ob_2_5,Ob_3_5,Ob_4_5,Ob_5_5,Ob_6_5,Ob_7_5,Ob_8_5)
       player.hitbox.center = (360, 70)
       fade(WIDTH, HEIGHT)

 def Level_5(self):

    if player.hitbox.centery > 590 and En1_5 not in enemys_level5 and En2_5 not in enemys_level5 and En3_5 not in enemys_level5 and En4_5 not in enemys_level5: 
       self.state = 'Level_6'
       player.hitbox.center = (460, 50)
       fade(WIDTH, HEIGHT)
       wall_list.empty()
       wall_list.add(Ob_1_4,Ob_2_4)


    enemys_level5.update()
    all_sprites.update()

    levelbild('img/levels/Level5.png')

    enemys_level5.draw(WIN)
    all_sprites.draw(WIN)
    
    dark_back.draw(WIN)
    dark_back.update()

    level5_trees.update()
    level5_trees.draw(WIN)

    Hp.update()
    Hp.draw(WIN)
 
 def Level_6(self):
    
    if player.hitbox.centery > 590: 
       self.state = 'Level_7'
       player.hitbox.center = (400, 500)
       fade(WIDTH, HEIGHT)
       wall_list.empty()
       wall_list.add(Ob_1_7,Ob_2_7,Ob_3_7,Ob_4_7,Ob_5_7,Ob_6_7,Ob_7_7,Ob_8_7,Ob_9_7,Ob_10_7,Ob_11_7)
       player.status = 'go_up_idle'
       all_sprites.update()
       self.image = pygame.image.load('the_code/aps/go_up_idle/walk up1.png').convert_alpha()
       self.image = pygame.transform.scale(self.image,(220, 270))
       
    if player.hitbox.centery < 10: 
         self.state = 'Level_5'
         player.hitbox.center = (450, 580)
         fade(WIDTH, HEIGHT)
         wall_list.empty()
         wall_list.add(Ob_1_5,Ob_2_5,Ob_3_5,Ob_4_5,Ob_5_5,Ob_6_5)

    all_sprites.update()

    levelbild('img/levels/LEVEL6_TEST.png')

    all_sprites.draw(WIN)

    dark_back.draw(WIN)
    dark_back.update()

    chests_all.update()
    chests_all.draw(WIN)

    est2.update()
    est2.draw(WIN)

    Hp.update()
    Hp.draw(WIN)

 def Level_7(self):

    all_sprites.update()
    enemys_level7.update()
    
    levelbild('img/levels/level7.png')

    all_sprites.draw(WIN)
    enemys_level7.draw(WIN)

    dark_back.draw(WIN)
    dark_back.update()

    level7_trees.update()
    level7_trees.draw(WIN)

    if EnBoss_7 not in enemys_level7:
      self.n += 50 
      player.kill()
      dark_forest.stop()
      victory.play()

      if self.n < 550: 
         cookie.image = pygame.transform.scale(cookie.image,(self.n, self.n))
         WIN.blit(cookie.image, (200, 0))
         t.sleep(0.1)

      if self.n > 600:
         levelbild('img/sener/heres cookie.png')
         pygame.display.update()
         t.sleep(5)
         levelbild('img/sener/duKlaradeDet_v2.png')
         pygame.display.update()
         t.sleep(5)
         pygame.quit()
         sys.exit()

    Hp.update()
    Hp.draw(WIN)

 def state_manager(self):
  if self.state == 'intro':
     self.intro()

  if self.state == 'Level_2':
     self.Level_2()
     
  if self.state == 'Level_3':
     self.Level_3()

  if self.state == 'frogHouse':
     self.frogHouse()   
   
  if self.state == 'Level_4':
     self.Level_4()

  if self.state == 'Level_5':
     self.Level_5()

  if self.state == 'Level_6':
     self.Level_6()

  if self.state == 'Level_7':
     self.Level_7()

the_game = the_Game() 