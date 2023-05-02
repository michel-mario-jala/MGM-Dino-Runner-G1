import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update (self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS)) 
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                print("BOOMM")
                pygame.time.delay(5000)
                game.playing = False
                     
    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
                       