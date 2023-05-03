
import pygame
class Menu:
    def __init__(self):
        pass
    
    def update_menu(self, font_t, text_t , center_X, center_Y,screen):
        values1, values2 = font_t
        font = pygame.font.Font(values1, values2)
        
        textV1, textV2, textV3 = text_t
        self.text = font.render(textV1, textV2, textV3)
        text_rect = self.text.get_rect()
        text_rect.center = (center_X, center_Y)
        screen.blit(self.text, text_rect)
        