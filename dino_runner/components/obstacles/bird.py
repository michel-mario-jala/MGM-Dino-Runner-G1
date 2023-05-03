
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    POS_Y_BIRD = 250
    
    def __init__(self):
        image = BIRD[0]
        super().__init__(image)
        self.rect.y = self.POS_Y_BIRD
        self.step = 0
       
    def update(self):
        if self.step >=10:
            self.step = 0
                
    def draw(self, screen):
        screen.blit(self.image[self.step // 5], self.rect)
        self.step += 1  
         