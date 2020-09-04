import pygame
from EventHandler import EventHandler
from Lander import Lander
from Controller import Controller


class GameLoop:

    def __init__(self):
        self.Controller = Controller()
        self.Handler = EventHandler(self.Controller)


    def init(self, config_data):
        # used to initialise the pygame library
        pygame.init()
        self.screen = pygame.display.set_mode((int(config_data['ScreenHeight']), int(config_data['ScreenWidth'])))
        pygame.display.set_caption('CE889 Assignment Template')
        self.screen.fill([255,255,255]) # adding white background


    def mainLoop(self):
        lander = Lander([0,0]) # Creates the lander object
        # The main loop of the window
        while True:
            self.Handler.handle(pygame.event.get())
            # update the list of things to be drawn on screen

            self.screen.blit(lander.image, lander.rect)
            # then update the visuals on screen from the list
            pygame.display.update()
