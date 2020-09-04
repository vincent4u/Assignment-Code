import pygame
from EventHandler import EventHandler


class GameLoop:

    def __init__(self):
        self.Handler = EventHandler()


    def init(self, config_data):
        # used to initialise the pygame library
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((int(config_data['ScreenHeight']), int(config_data['ScreenWidth'])))
        pygame.display.set_caption('CE889 Assignment Template')


    def mainLoop(self):
        # The main loop of the window
        while True:
            self.Handler.handle(pygame.event.get())
            # update the visuals on screen
            pygame.display.update()
