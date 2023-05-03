
from dino_runner.components.menu import Menu

class Score:
    def __init__(self):
        self.SCORE_FINAL = 0
        self.score = 0
        self.menu = Menu()
        
    def update (self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2    
            
    def draw(self, screen):
        self.menu.update_menu(('freesansbold.ttf', 22), ((f"Score: {self.score}"), True, (0,0,0) ) , 1000, 50, screen )
       # font = pygame.font.Font('freesansbold.ttf', 22)
        #text = font.render(f"Score: {self.score}", True, (0,0,0) )
        #text_rect = text.get_rect()
        #text_rect.center = (1000, 50)
        #screen.blit(text, text_rect)        