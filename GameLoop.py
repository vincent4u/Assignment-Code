import pygame, time, ctypes, sys
from EventHandler import EventHandler
from Lander import Lander
from Controller import Controller
from Vector import Vector
from GameLogic import GameLogic
from Surface import Surface
from Menu import Menu


class GameLoop:

    def __init__(self):
        self.Controller = Controller()
        self.Handler = EventHandler(self.Controller)
        self.object_list = []
        self.game_logic = GameLogic()
        self.fps_clock = pygame.time.Clock()
        self.fps = 60

    def init(self, config_data):
        # used to initialise the pygame library
        pygame.init()
        if config_data["FULLSCREEN"] == "TRUE":
            user32 = ctypes.windll.user32
            config_data['SCREEN_HEIGHT'] = int(user32.GetSystemMetrics(1))
            config_data['SCREEN_WIDTH'] = int(user32.GetSystemMetrics(0))
            self.screen = pygame.display.set_mode((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']),
                                                  pygame.FULLSCREEN)
        else:
            config_data['SCREEN_HEIGHT'] = int(config_data['SCREEN_HEIGHT'])
            config_data['SCREEN_WIDTH'] = int(config_data['SCREEN_WIDTH'])
            self.screen = pygame.display.set_mode((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))
        pygame.display.set_caption('CE889 Assignment Template')
        pygame.display.set_icon(pygame.image.load(config_data['LANDER_IMG_PATH']))



    def main_loop(self, config_data):
        # create the group for visuals to be updated
        sprites = pygame.sprite.Group()

        # booleans for what the game state is
        on_menus = False
        game_start = True


        if on_menus:
            self.menu(config_data, sprites)
        # The main loop of the window
        background_image = pygame.image.load(config_data['BACKGROUND_IMG_PATH'])
        background_image = pygame.transform.scale(background_image, (config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))

        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS', 30)


        while True:
            self.Handler.handle(pygame.event.get())
            # update the list of things to be drawn on screen
            # painting white background
            #self.screen.fill([0, 255, 255])
            self.screen.blit(background_image,(0,0))

            if on_menus:
                self
            else:
                if game_start:
                    sprites = pygame.sprite.Group()
                    self.game_start(config_data, sprites)
                    game_start = False
                self.update_objects()
                # check if lander collided with surface
                if (self.lander.surface_collision(self.surface)):
                    pygame.quit()
                    sys.exit()
            # then update the visuals on screen from the list
            sprites.draw(self.screen)
            # surface_sprites.draw(self.screen)
            Fps_count = str(self.fps_clock)
            FpsText = "FPS: " + Fps_count
            textsurface = myfont.render(FpsText, False, (255, 255, 255))
            self.screen.blit(textsurface, (0, 0))
            pygame.display.flip()
            self.fps_clock.tick(self.fps)

    def update_objects(self):
        # update the speeds and positions of the objects in game
        self.game_logic.update(0.2)

    def setup_lander(self, config_data):
        lander = Lander(config_data['LANDER_IMG_PATH'],
                        [config_data['SCREEN_WIDTH'] / 2, config_data['SCREEN_HEIGHT'] / 2], Vector(0, 0),
                        self.Controller)
        self.game_logic.add_lander(lander)
        return lander

    def game_start(self, config_data, sprites):
        # Creates the lander object
        self.lander = self.setup_lander(config_data)
        self.surface = Surface((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))
        sprites.add(self.lander)
        sprites.add(self.surface)

    def menu(self, config_data, sprites):
        print(config_data)
        menu = Menu((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))
        sprites.add(menu)
