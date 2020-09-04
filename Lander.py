import pygame

class Lander(pygame.sprite.Sprite):
    def __init__(self, filepath, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
