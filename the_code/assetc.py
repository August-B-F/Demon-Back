import pygame
import sys 
import os
import time as t
import math
import threading
from pygame import image

from the_code.constants import *

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
 
class wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.hitbox = self.rect

class frogH(pygame.sprite.Sprite): 
    def __init__(self, image_path, rect_x, rect_y):

      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(os.path.join(game_folder, image_path)).convert()
      self.image = pygame.transform.scale(self.image,(200, 150))
      self.image.set_colorkey(BLACK)
      self.image.set_alpha(0)
      self.rect = self.image.get_rect()
      self.rect.center = (rect_x, rect_y)

class ut(pygame.sprite.Sprite): 
    def __init__(self, image_path, rect_x, rect_y):

      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(os.path.join(game_folder, image_path)).convert()
      self.image = pygame.transform.scale(self.image,(40, 40))
      self.image.set_colorkey(BLACK)
      self.image.set_alpha(0)
      self.rect = self.image.get_rect()
      self.rect.center = (rect_x, rect_y)

class frogdoor(pygame.sprite.Sprite): 
    def __init__(self, image_path, rect_x, rect_y):

      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(os.path.join(game_folder, image_path)).convert()
      self.image = pygame.transform.scale(self.image,(30, 30))
      self.image.set_colorkey(BLACK)
      self.image.set_alpha(0)
      self.rect = self.image.get_rect()
      self.rect.center = (rect_x, rect_y)

class mob(pygame.sprite.Sprite):

    def __init__(self, image_path, rect_x, rect_y,x ,y):

      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(os.path.join(game_folder, image_path)).convert()
      self.image = pygame.transform.scale(self.image,(x, y))
      self.image.set_colorkey(BLACK)
      self.image.set_alpha(0)
      self.rect = self.image.get_rect()
      self.rect.center = (rect_x, rect_y)
        
class Darken(pygame.sprite.Sprite):

    def __init__(self, image_path, rect_x, rect_y):

      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(os.path.join(game_folder, image_path)).convert()
      self.image = pygame.transform.scale(self.image,(WIDTH, HEIGHT))
      self.image.set_colorkey(WHITE)
      self.rect = self.image.get_rect()
      self.rect.center = (rect_x, rect_y)

class mellan(pygame.sprite.Sprite):

    def __init__(self, image_path, rect_x, rect_y, width, height):

       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(game_folder, image_path)).convert()
       self.image = pygame.transform.scale(self.image,(width, height))
       self.image.set_colorkey(RED)
       self.rect = self.image.get_rect()
       self.rect.center = (rect_x, rect_y)

#frog (<:
class NPC(pygame.sprite.Sprite):
    def __init__(self, image_path, rect_x, rect_y):

       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(game_folder, image_path)).convert()
       self.image = pygame.transform.scale(self.image,(50, 50))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()
       self.rect.center = (rect_x, rect_y)
       self.ani = False
       self.ani_farme = 0 
       self.timer = 49 

    def update(self):

      self.timer += 1
      if self.timer >= 30: 

          if self.ani_farme > 3:
            self.ani_farme = 0

          frog.image = NPC_ani[self.ani_farme]
          frog.image = pygame.transform.scale(frog.image,(50, 50))        
          self.ani_farme += 1
          self.timer = 0 

def fade(width, height): 

  fade = pygame.Surface((width, height))
  fade.fill((BLACK))

  for alpha in range(0, 255, 85):
    fade.set_alpha(alpha)
    WIN.blit(fade, (0,0))
    pygame.display.update()
    pygame.time.delay(300)


def redfade(width, height): 

  fade = pygame.Surface((width, height))
  fade.fill((RED))

  for alpha in range(0, 50):
    
    fade.set_alpha(alpha)
    WIN.blit(fade, (0,0))
    pygame.display.update()
    pygame.time.delay(50)


######################################Allt här läger saker i klasser#####################################################################
dooren = pygame.sprite.Group()
house = pygame.sprite.Group() 
mobs = pygame.sprite.Group()
tillbaka = pygame.sprite.Group()
enemys_level5 = pygame.sprite.Group()
chestB = pygame.sprite.Group()
overgang = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
Hp  = pygame.sprite.Group()
objects  = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
est = pygame.sprite.Group()
est2 = pygame.sprite.Group()
dark_back = pygame.sprite.Group()
enemys_level7 = pygame.sprite.Group()
chests_all= pygame.sprite.Group()
level5_trees = pygame.sprite.Group()
level7_trees = pygame.sprite.Group()
level1_till = pygame.sprite.Group()
fish = pygame.sprite.Group()

m2 = mob(image_path="img/farger/transparant.png", rect_x=450, rect_y= 520, x=80, y=20)
mH = frogH(image_path="img/farger/transparant.png", rect_x=200, rect_y= 150)
door = frogdoor(image_path="img/farger/transparant.png", rect_x=240, rect_y= 168)
till = ut(image_path="img/farger/transparant.png", rect_x=455, rect_y= 400)
tillfrog = mob(image_path="img/NPC/till frog_v4.png", rect_x=550, rect_y= 110, x=80, y=20)
tillfrog.image.set_alpha(255)
tillfrog.image = pygame.transform.scale(tillfrog.image,(44, 42))

keys = Darken(image_path="img/sener/keys.png", rect_x = 750, rect_y = 435)
keys.image = pygame.transform.scale(keys.image,(100, 100))
shift = Darken(image_path="img/sener/shift.png", rect_x = 850, rect_y = 450)
shift.image = pygame.transform.scale(shift.image,(100, 100))
space = Darken(image_path="img/sener/space.png", rect_x = 950, rect_y = 435)
space.image = pygame.transform.scale(space.image,(170, 120))

cookie = Darken(image_path="img/sener/cookie_v2.png", rect_x = 450, rect_y = 300)

rod = mellan(image_path="img/farger/red.png", rect_x= 400, rect_y= 300, width=1200, height=1800)

tillLevel1 = Darken(image_path="img/levels/TillLevel1_v5.png", rect_x = 450, rect_y = 300)

dark = Darken(image_path="img/levels/darken.png", rect_x = 450, rect_y = 300)
dark.image.set_alpha(70)

Chad = Darken(image_path="img/levels/trees_level_4.png", rect_x=450, rect_y= 300)
dark2 = Darken(image_path="img/farger/svart.png", rect_x = 450, rect_y = 300)
dark2.image.set_alpha(70)

frog_test = Darken(image_path="img/Extras/frog_test_v3.png", rect_x=450, rect_y= 300)

tress_5 = Darken(image_path="img/levels/Tress_level5.png", rect_x = 450, rect_y = 300)
level5_trees.add(tress_5)

tress_7 = Darken(image_path="img/levels/Tress_level7.png", rect_x = 450, rect_y = 300)
level7_trees.add(tress_7)

mr_f = Darken(image_path="img/sener/Mr_F.png", rect_x = 450, rect_y = 300)
all_sprites.add(mr_f)

frog = NPC(image_path="img/NPC/frog1.png", rect_x=550, rect_y= 170)

####################VÄGAR###############################

# Level 1 
Ob_1_1 = wall(780, 0, 60, HEIGHT)
ob_2_1 = wall(0, 45, WIDTH, 30)
Ob_3_1 = wall(50, 0, 60, HEIGHT)
ob_4_1 = wall(0, 520, WIDTH, 30)
wall_list.add(Ob_1_1, ob_2_1, Ob_3_1, ob_4_1)

#Level 2
Ob_1_2 = wall(260, 0, 60, HEIGHT)
Ob_2_2 = wall(625, 0, 60, HEIGHT)
ob_3_2 = wall(0, 60, WIDTH, 10)

Ob_4_2 = wall(582, 127, 30, 30)
Ob_5_2 = wall(375, 244, 30, 30)
ob_6_2 = wall(573, 307, 30, 30)
Ob_7_2 = wall(375, 487, 30, 30)
Ob_8_2 = wall(573, 508, 50, 50)

#Level 3
Ob_1_3 = wall(800, 0, 110, HEIGHT)
Ob_2_3 = wall(50, 0, 60, HEIGHT)
Ob_3_3 = wall(0, 0, 700, 110)
Ob_4_3 = wall(0, 540, 720, 140)
Ob_5_3 = wall(110, 100, 190, 80)

Ob_6_3 = wall(395, 150, 30, 30)
Ob_7_3 = wall(100, 320, 610, 40)
Ob_8_3 = wall(100, 360, 400, 80)
Ob_9_3 = wall(100, 440, 620, 80)
Ob_10_3 = wall(530, 100, 40, 90)
Ob_11_3 = wall(700, 600, 300, 30)

#froghouse
Ob_1_frog = wall(220, 0, 60, HEIGHT)
Ob_2_frog = wall(615, 0, 60, HEIGHT)
ob_3_frog = wall(0, 240, WIDTH, 10)
Ob_7_frog = wall(0, 385, WIDTH, 30)

Ob_4_frog = wall(280, 200, 100, 110)
Ob_5_frog = wall(380, 240, 60, 45)
ob_6_frog = wall(490, 290, 30, 30)
Ob_8_frog = wall(520, 240, 100, 90)

#Level 4
Ob_1_4 = wall(240, 0, 100, HEIGHT)
Ob_2_4 = wall(590, 0, 100, HEIGHT)

#Level 5
Ob_1_5 = wall(114, 530, 186, 70)
Ob_2_5 = wall(98, 100, 18, 450)
Ob_3_5 = wall(100, 0, 170, 100)
Ob_4_5 = wall(800, 0, 100, HEIGHT)
Ob_5_5 = wall(420, 0, 400, 100)
Ob_6_5 = wall(550, 550, 300, 50)
Ob_7_5 = wall(0, -10, 900, 50)
Ob_8_5 = wall(0, 640, 900, 50)

#level 7
Ob_1_7 = wall(114, 530, 186, 70)
Ob_2_7 = wall(98, 126, 18, 404)
Ob_3_7 = wall(114, 126, 110, 10)
Ob_4_7 = wall(216, 134, 130, 16)
Ob_5_7 = wall(334, 50, 20, 86)
Ob_6_7 = wall(355, 70, 120, 20)
Ob_7_7 = wall(475, 70, 400, 70)
Ob_8_7 = wall(600, 130, 80, 40)
Ob_9_7 = wall(785, 100, 60, 500)
Ob_10_7 = wall(540, 550, 300, 70)
Ob_11_7 = wall(0, 600, 900, 10)

#fisk 
Fing = mob(image_path="img/sener/e.png", rect_x=480, rect_y= 400,x=50,y=50)

overgang.add(rod)
mobs.add(m2)
house.add(mH)
dooren.add(door)
tillbaka.add(till)
chestB.add(frog)
chestB.add(tillfrog)

est.add(dark)
est.add(Chad)

dark_back.add(dark2)
est2.add(Chad)

level1_till.add(tillLevel1)