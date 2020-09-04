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
            if event.type == KEYDOWN:
                self.KeyboardController(event)

    def KeyboardController(self, event):
        # Key Board Controller
        if(event.key == 273):
            print("Arrow Up")
        if (event.key == 276):
            print("Arrow Left")
        if (event.key == 275):
            print("Arrow Right")

