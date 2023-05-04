
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    POS_Y_BIRD = [250, 290]
    def __init__(self):
        image = BIRD[0]
        super().__init__(image)
        self.rect.y = random.choice(self.POS_Y_BIRD)
        self.step = 0
       
    def update(self, game_speed, obstacles):
        if self.step >=10:
            self.step = 0
        return super().update(game_speed, obstacles)
                
    def draw(self, screen):
        self.image = BIRD[self.step // 5]
        self.step += 1 
        return super().draw(screen)     