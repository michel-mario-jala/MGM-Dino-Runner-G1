
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD

class Birds(Obstacle):
    POS_Y_BIRD = 250
    
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = self.POS_Y_BIRD
        self.step = 0
       
    def draw(self, screen):
        if self.step >=10:
            self.step = 0    
        screen.blit(BIRD[self.step // 5], self.rect)
        self.step += 1  
         