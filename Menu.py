import pygame


class Menu(pygame.sprite.Sprite):

    def __int__(self, screen_dimension):
        pygame.sprite.Sprite.__init__(self)
        # create the points for the buttons
        self.button = self.create_button()

        # create the canvas where the polygon will be painted, make it
        self.image = pygame.Surface([screen_dimension[0], screen_dimension[1]])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        # create the buttons using the points
        self.polygon_rect = pygame.draw.polygon(self.image, (0, 0, 0), self.button)

        self.rect = self.image.get_rect()

    def create_button(self, height, width, x, y):
        return [(0, 110), (0, 500), (500, 120)]
