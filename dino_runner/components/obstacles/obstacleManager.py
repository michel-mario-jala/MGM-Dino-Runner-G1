import pygame
import random
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update (self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                self.obstacles.append(Birds(BIRD))    
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                print("BOOMM")
                pygame.time.delay(500)
                game.playing = False
                     
    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
                       