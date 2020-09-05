import pygame

class Surface(pygame.sprite.Sprite):

    def __init__(self, screen_dimension, location):
        pygame.sprite.Sprite.__init__(self)

        self.x = location[0]
        self.y = location[1]

        self.image = pygame.Surface([screen_dimension[0],screen_dimension[1]])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))

        # pygame.draw.rect(self.image, (255,0,0), [0,0,200,5])

        self.rect = pygame.draw.polygon(self.image, (0,0,0), [(0,0), (screen_dimension[0], 0), (screen_dimension[0], screen_dimension[1]), (0, screen_dimension[1])])        
        
        # self.rect = pygame.draw.line(screen, (255,0,0), start_point, end_point, 5)
        # self.rect.x = start_point[0]
        # self.rect.y = start_point[1]