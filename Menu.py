import pygame

class Menu:

    def __int__(self):

        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.GRAY = (128,128,128)


    def draw_buttons(self, screen):
        top_left = (300, 200)
        FONT = pygame.font.SysFont("Times New Norman", 60)
        text_buttons = [FONT.render("Play Game", True, (255,255,255)), "Data Collection", "Quit"]
        rect_buttons = [(top_left[0], top_left[1], 200, 80),(top_left[0], top_left[1]+100, 200, 80), (top_left[0], top_left[1]+200, 200, 80)]
        
        buttons = [
            [text_buttons[0], rect_buttons[0], (0,0,0)],
        ]
        screen.fill((255,255,255))
        for text, rect, color in buttons:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)