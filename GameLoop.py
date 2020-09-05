import pygame, time, ctypes
from EventHandler import EventHandler
from Lander import Lander
from Controller import Controller
from Vector import Vector
from GameLogic import GameLogic
from Surface import Surface


class GameLoop:

    def __init__(self):
        self.Controller = Controller()
        self.Handler = EventHandler(self.Controller)
        self.object_list = []
        self.game_logic = GameLogic()


    def init(self, config_data):
        # used to initialise the pygame library
        pygame.init()
        if config_data["FULLSCREEN"] == "TRUE":
            print(config_data)
            user32 = ctypes.windll.user32
            self.screen = pygame.display.set_mode((int(user32.GetSystemMetrics(0)), int(user32.GetSystemMetrics(1))),pygame.FULLSCREEN)
            config_data['SCREEN_HEIGHT'] = int(user32.GetSystemMetrics(0))
            config_data['SCREEN_WIDTH'] = int(user32.GetSystemMetrics(1))
            print(config_data)

        else:
            config_data['SCREEN_HEIGHT'] = int(config_data['SCREEN_HEIGHT'])
            config_data['SCREEN_WIDTH'] = int(config_data['SCREEN_WIDTH'])
            self.screen = pygame.display.set_mode((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))
        pygame.display.set_caption('CE889 Assignment Template')
        pygame.display.set_icon(pygame.image.load(config_data['LANDER_IMG_PATH']))


    def main_loop(self, config_data):
        # Creates the lander object
        lander = self.setup_lander(config_data)
        # surface = Surface(self.screen, (100,100), (200,200))
        print(config_data['SCREEN_WIDTH'])
        surface = Surface((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']*.2), (0,50))
        # surface_sprites = pygame.sprite.Group()
        sprites = pygame.sprite.Group()
        sprites.add(lander)
        sprites.add(surface)
        # surface_sprites.add(surface)


        # The main loop of the window
        while True:
            self.Handler.handle(pygame.event.get())
            # update the list of things to be drawn on screen
            self.update_objects()
            # painting white background
            self.screen.fill([255, 255, 255])

            # pygame.draw.line(self.screen, (255,0,0), (100,100), (200,200), 5)
            # then update the visuals on screen from the list
            sprites.draw(self.screen)
            # surface_sprites.draw(self.screen)
            pygame.display.update()
            time.sleep(0.06)

    def update_objects(self):
        # update the speeds and positions of the objects in game
        self.game_logic.update(0.2)

    def setup_lander(self, config_data):
        lander = Lander(config_data['LANDER_IMG_PATH'], [config_data['SCREEN_HEIGHT']/2,config_data['SCREEN_WIDTH']/2 ], Vector(0, 0), self.Controller)
        self.game_logic.add_lander(lander)
        return lander
