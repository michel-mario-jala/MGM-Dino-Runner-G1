
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update (self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            obstacle_random = random.randint(0,1)
            if  obstacle_random == 0:
                self.obstacles.append(Cactus())
            elif obstacle_random == 1 :
                self.obstacles.append(Bird())
                     
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                on_death()
                     
    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset(self):
        self.obstacles = []                   