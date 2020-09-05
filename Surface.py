import pygame

class Surface(pygame.sprite.Sprite):

    def __init__(self, screen, start_point, end_point):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([200,5])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))

        pygame.draw.rect(self.image, (255,0,0), [0,0,200,5])

        self.rect = self.image.get_rect()

        # self.rect = pygame.draw.line(screen, (255,0,0), start_point, end_point, 5)
        # self.rect.x = start_point[0]
        # self.rect.y = start_point[1]