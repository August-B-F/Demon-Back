from pickle import FALSE
import pygame 

from math import sin
from the_code.constants import *
from the_code.assetc import *
from the_code.Sound import *
from csv import reader
from os import walk

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()

    self.image = pygame.image.load('the_code/aps/go_down_idle/walk down1.png').convert_alpha()
    self.image = pygame.transform.scale(self.image,(220, 270))

    self.rect = self.image.get_rect(topleft = (x, y))
    self.hitbox = self.rect.inflate(-190,-220)
    self.attack_radios = self.rect.inflate(-180,-210)

    self.import_player_assets()
    self.status = 'go_down'
    self.direction = pygame.math.Vector2()
    self.frame_index = 0
    self.animation_speed = 0.15

    self.can_walk = True
    self.vulnerable = True
    self.attacking = False

    self.invulnerability_duration = 500
    self.attack_cooldown = 200
    self.doge_cooldown = 1000
    self.attack_time = None
    self.doge_time = None
    self.hurt_time = None
    self.walls = None

    self.atc = False 
    self.can_doge = True
    self.dash = False

    self.stat_info = player_stats
    self.health = self.stat_info['health']
    self.speed = self.stat_info['speed']
    self.atcpoints = self.stat_info['attack']
    self.dogespeed = self.stat_info['dogespeed']
  
  def move(self):
    if self.direction.magnitude() != 0:
      self.direction = self.direction.normalize()
    
    if self.dash:
      self.vulnerable = False

      if 'attack' in self.status or 'idle' in self.status:
        self.hitbox.centerx += 0

      elif 'go_right' in self.status:
        self.hitbox.centerx += 50

      elif 'go_left' in self.status:
        self.hitbox.centerx -= 50

      elif 'go_up' in self.status:
        self.hitbox.centery -= 50

      else:
        self.hitbox.centery += 50

    else:

      self.hitbox.x += self.direction.x * self.speed
      self.collision('horizontal')
      self.hitbox.y += self.direction.y * self.speed
      self.collision('vertical')
      self.rect.center = self.hitbox.center
      self.attack_radios.center = self.hitbox.center

  def input(self):

    key = pygame.key.get_pressed()

    if player.hitbox.colliderect(Fing) and Fing in fish: 
      
        Fing.image.set_alpha(255)
        fish.add(Fing)

        if key[pygame.K_e]:

          fade(WIDTH, HEIGHT)

          levelbild('img/sener/out_fishing.png')
          pygame.display.update()
          t.sleep(2)

          levelbild('img/sener/big_thing.png')
          pygame.display.update()
          t.sleep(2)

          levelbild('img/sener/sad.png')
          pygame.display.update()
          t.sleep(2)
    else:
      Fing.image.set_alpha(0)
      

    if key[pygame.K_LSHIFT] and self.can_doge:
      self.doge_time = pygame.time.get_ticks()
      shift.kill()
      self.dash = True
      self.can_doge = False

    elif not self.can_doge:
      self.dash = False

    if key[pygame.K_UP] or key[pygame.K_w]:
      self.direction.y -= 1
      self.status = 'go_up'
      keys.kill()

    elif key[pygame.K_DOWN] or key[pygame.K_s]:
      self.direction.y += 1
      self.status = 'go_down'
      keys.kill()

    else:
      self.direction.y = 0

    if key[pygame.K_LEFT] or key[pygame.K_a]:
      self.direction.x -= 1
      self.status = 'go_left'
      keys.kill()

    elif key[pygame.K_RIGHT] or key[pygame.K_d]:
      self.direction.x += 1
      self.status = 'go_right'
      keys.kill()

    else:
      self.direction.x = 0

    if key[pygame.K_SPACE]:
      if not self.attacking:
         sword.play()

      self.attacking = True
      self.attack_time = pygame.time.get_ticks()
      space.kill()

  def import_player_assets(self):
    character_path = 'the_code/aps/'

    self.animations = {'go_up': [],'go_down': [],'go_left': [],'go_right': [],
			'go_right_attack':[],'go_left_attack':[],'go_up_attack':[],'go_down_attack':[],
      'go_right_idle':[],'go_left_idle':[],'go_up_idle':[],'go_down_idle':[],'go_left_fishing':[]}

    for animation in self.animations.keys():

      full_path = character_path + animation
      self.animations[animation] = import_folder(full_path)

  def animate(self):
    
    animation = self.animations[self.status]

    self.frame_index += self.animation_speed

    if self.frame_index >= len(animation):
      self.frame_index = 0

    self.image = animation[int(self.frame_index)]
    self.image = pygame.transform.scale(self.image,(220, 270))
    self.rect = self.image.get_rect(center = self.hitbox.center)

  def get_status(self):

    if self.direction.x == 0 and self.direction.y == 0:

      if not 'idle' in self.status and not '_attack' in self.status:
        self.status = self.status + '_idle'

    if self.attacking:
      self.direction.x = 0
      self.direction.y = 0

      if not 'attack' in self.status:

        if 'idle' in self.status:
          self.status = self.status.replace('_idle','_attack')

        else:
          self.status = self.status + '_attack'

    else:

      if 'attack' in self.status:
        self.status = self.status.replace('_attack','')

  
  def collision(self,direction): 
    if direction == 'horizontal':
      for sprite in self.walls:
        if sprite.hitbox.colliderect(self.hitbox):
          if self.direction.x > 0: 
            self.hitbox.right = sprite.hitbox.left
          if self.direction.x < 0: 
            self.hitbox.left = sprite.hitbox.right

    if direction == 'vertical':
      for sprite in self.walls:
        if sprite.hitbox.colliderect(self.hitbox):
          if self.direction.y > 0: 
            self.hitbox.bottom = sprite.hitbox.top
          if self.direction.y < 0: 
            self.hitbox.top = sprite.hitbox.bottom

  def cooldowns(self):
    current_time = pygame.time.get_ticks()
    
    if self.attacking:
      if current_time - self.attack_time >= self.attack_cooldown:
        self.attacking = False
    
    if not self.can_doge:
      if current_time - self.doge_time >= self.doge_cooldown:
        self.can_doge = True


  def update(self):
    self.input()
    self.cooldowns()
    self.get_status()
    self.animate()
    self.move()

   
class Player_health(pygame.sprite.Sprite):

	def __init__(self):

		super().__init__()
		self.image = pygame.Surface((40,40))
		self.rect = self.image.get_rect(center = (1, -400))
		self.current_health = 1000 
		self.target_health = 1000
		self.max_health = 1000
		self.health_bar_length = 300
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = 10

	def get_damage(self,amount):

		if self.target_health > 0:
			self.target_health -= amount

		if self.target_health < 0:
			self.target_health = 0

	def get_health(self,amount):

		if self.target_health < self.max_health:
			self.target_health += amount
      
		if self.target_health > self.max_health:
			self.target_health = self.max_health

	def update(self):
		self.advanced_health()

	def advanced_health(self):
		transition_width = 0
		transition_color = (155,0,0)

		if self.current_health < self.target_health:
			self.current_health += self.health_change_speed
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (0,155,0)

		if self.current_health > self.target_health:
			self.current_health -= self.health_change_speed 
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (70,80,100)

		health_bar_width = int(self.current_health / self.health_ratio)
		health_bar = pygame.Rect(580,20,health_bar_width,20)
		transition_bar = pygame.Rect(health_bar.right,20,transition_width,20)
		
		pygame.draw.rect(WIN,(155,0,0),health_bar)
		pygame.draw.rect(WIN,transition_color,transition_bar)	
		pygame.draw.rect(WIN,(70,80,100),(580,20,self.health_bar_length,20),4)	

player = Player(340, 130)
all_sprites.add(player)
player.walls = wall_list
player_health = Player_health()
Hp.add(player_health)

