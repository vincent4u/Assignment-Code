import pygame

class Menu(pygame.sprite.Sprite):

    def __int__(self, screen_dimension):
        print("Menu open")
        pygame.sprite.Sprite.__init__(self)
        # create the image buttons

        button = self.create_button()

        self.image = pygame.Surface([screen_dimension[0], screen_dimension[1]])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))

        pygame.draw.polygon(self.image, (0, 0, 0), button)

        self.rect = self.image.get_rect()

    def create_button(self, height, width, x, y):
        return [(0,110), (0,500), (500, 120)]