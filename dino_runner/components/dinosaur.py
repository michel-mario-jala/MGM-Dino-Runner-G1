import pygame
from pygame.sprite import Sprite
from dino_runner.components.menu import update_menu
from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_SHIELD, JUMPING, JUMPING_SHIELD, RUNNING, RUNNING_SHIELD, SHIELD_TYPE

JUMP_VELOCITY = 8.5
DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"

DUCKING_IMG = {DEFAULT_TYPE : DUCKING, SHIELD_TYPE : DUCKING_SHIELD}
JUMPING_IMG = {DEFAULT_TYPE : JUMPING, SHIELD_TYPE : JUMPING_SHIELD}
RUNNING_IMG = {DEFAULT_TYPE : RUNNING, SHIELD_TYPE : RUNNING_SHIELD}

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    POS_Y_DUCK = 340
    
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUNNING_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = JUMP_VELOCITY
    
    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()    
        
        if self.action != DINO_JUMPING :
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING         
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING
            
        if self.step >=10:
            self.step = 0
    
    def duck(self):
        self.image = DUCKING_IMG[self.type] [self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y_DUCK
        self.step += 1
        
    def jump(self):
        self.image = JUMPING_IMG[self.type]
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8 
        print(self.rect.y, self.jump_velocity, sep= "::")   
        if self.jump_velocity < -JUMP_VELOCITY:
            self.rect.y = self.POS_Y
            self.action = DINO_RUNNING
            self.jump_velocity = JUMP_VELOCITY
    
    def run(self):
        self.image = RUNNING_IMG[self.type][self.step // 5]
        self.step += 1
        self.rect.y = self.POS_Y
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.star_time + (power_up.duration * 1000)
        print("powerUPps")
        print(power_up.type)
    
    def draw_power_up(self, screen):
        if self.type != DEFAULT_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                update_menu(
                    f"{screen, self.type.capitalize()} enable for {time_to_show} seconds.",
                    font_size = 22,
                    pos_y_center = 50)    
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0    