import pygame, sys
from pygame.locals import *


class EventHandler:

    def __init__(self, controller):
        self.controller = controller

    def handle(self, event_list):
        for event in event_list:
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                self.keyboard_controller_down(event)
            if event.type == KEYUP:
                self.keyboard_controller_up(event)


    def keyboard_controller_down(self, event):
        print(event.key)
        if event.key == 273:
            self.controller.set_up(True)
        if event.key == 276:
            self.controller.set_left(True)
        if event.key == 275:
            self.controller.set_right(True)
        if event.key == 113:
            self.quit();


    def keyboard_controller_up(self, event):
        if event.key == 273:
            self.controller.set_up(False)
        if event.key == 276:
            self.controller.set_left(False)
        if event.key == 275:
            self.controller.set_right(False)


    def quit(self):
        pygame.quit()
        sys.exit()
