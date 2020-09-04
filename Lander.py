import pygame

class Lander(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/lander.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
