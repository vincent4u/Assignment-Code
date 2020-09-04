import pygame, sys
from pygame.locals import *


class GameLoop:
    def init(self, config_data):
        # used to initialise the pygame library
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((config_data['ScreenHeight'], config_data['ScreenWidth']))
        pygame.display.set_caption('CE889 Assignment Template')
