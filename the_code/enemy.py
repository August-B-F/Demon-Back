import pygame
from the_code.constants import *
from the_code.spelare import player_health, player 
from math import sin

enemys_all= pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,monster_name,rect_x,rect_y,groups,w,h,name):
        super().__init__(groups)

        self.name = name
        self.monster_name = monster_name
        self.monster_info = monster_data[self.monster_name]
        self.image = pygame.image.load(os.path.join(game_folder, self.monster_info['img'])).convert()
        self.speed = self.monster_info['speed']
        self.health = self.monster_info['health']
        self.atcpoints = self.monster_info['damage']
        self.resistance = self.monster_info['resistance']
        
        self.image = pygame.transform.scale(self.image,(w, h))
        self.h = h 
        self.w = w
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (rect_x, rect_y)
        self.hitbox = self.rect.inflate(0,-10)
        
        self.can_attack = True
        self.vulnerable = True
        self.attack_time = None
        self.hit_time = None
        self.attack_cooldown = 300
        self.invincibility_duration = 500  
        self.ani_death = 0     
        self.timer = 0   

        self.allEnemy = enemys_all
    
    def move(self): 
      dirvect = pygame.math.Vector2(player.hitbox.centerx - self.rect.centerx, player.hitbox.centery - self.rect.centery)

      if dirvect.length() != 0:
        dirvect.normalize()
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)
        
        self.hitbox = self.rect.center

    def check_death(self):
        if self.health <= 0:
            self.timer += 1
            self.speed = 0 
            self.atcpoints = 0 
            self.image.set_alpha(255)
            if self.timer >= 5: 

                if self.ani_death > 5:
                    self.kill()
                    self.ani_death = 0 

                self.image = enemy_death_ani[self.ani_death]
                self.image = pygame.transform.scale(self.image,(self.w*2, self.h*2))        
                self.ani_death += 1
                self.timer = 0 

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 100: 
            return 255
        else: 
            return 100

    def collision(self):
        if player.hitbox.colliderect(self):
            self.speed = 0 
        else:
            self.speed = self.monster_info['speed']

        if player.hitbox.colliderect(self) and self.can_attack:
            self.attack_time = pygame.time.get_ticks()
            player_health.get_damage(self.atcpoints)
            self.can_attack = False

        if player.attacking and self.vulnerable and player.attack_radios.colliderect(self):
            self.hit_time = pygame.time.get_ticks()
            self.health -= player.atcpoints
            self.vulnerable = False
            self.speed = -self.resistance
        

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
        
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack: 
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

    def update(self):
        self.move()
        self.collision()
        self.cooldowns()
        self.check_death()