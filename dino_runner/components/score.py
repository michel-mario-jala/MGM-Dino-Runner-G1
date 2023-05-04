
from dino_runner.components.menu import update_menu

class Score:
    def __init__(self):
        self.SCORE_FINAL = 0
        self.score = 0
        
    def update (self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2    
            
    def draw(self, screen):
        update_menu(screen, f"Score: {self.score}", font_size= 22, pos_x_center = 1000, pos_y_center = 50 )
        
    def reset(self):
        self.score = 0           