import random
from dino_runner.components.obstacles.obstacles import Obstacle

class SmallCactus(Obstacle):
    POS_Y_SMALLCACTUS = 325
    
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = self.POS_Y_SMALLCACTUS
    
class LargeCactus(Obstacle):
    POS_Y_LARGECACTUS = 300
    
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = self.POS_Y_LARGECACTUS
        