import pygame, sys
from pygame.locals import *


class EventHandler:
    def __init__(self):
        self

    def handle(self, event_list):
        for event in event_list:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
