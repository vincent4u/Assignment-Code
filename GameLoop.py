import pygame, time, ctypes, sys
from EventHandler import EventHandler
from Lander import Lander
from Controller import Controller
from Vector import Vector
from GameLogic import GameLogic
from Surface import Surface
from MainMenu import MainMenu
from ResultMenu import ResultMenu
from DataCollection import DataCollection

class GameLoop:

    def __init__(self):
        self.controller = Controller()
        self.Handler = EventHandler(self.controller)
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
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module you need to call pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        
        # create the group for visuals to be updated
        sprites = pygame.sprite.Group()

        # booleans for what the game state is
        on_menus = [True, False, False] #Main, Won, Lost
        game_start = False

        # Game modes: Play Game, Data Collection, Neural Net, Quit
        game_modes = [False, False, False, False]
        
        # The main loop of the window
        background_image = pygame.image.load(config_data['BACKGROUND_IMG_PATH']).convert_alpha()
        background_image = pygame.transform.scale(background_image, (config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))

        data_collector = DataCollection()
        main_menu = MainMenu((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))
        result_menu = ResultMenu((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))
        # Initialize 
        while True:
            # check if Quit button was clicked
            if (game_modes[len(game_modes)-1]):
                pygame.quit()
                sys.exit()

            # if game is started, initialize all objects
            if game_start:
                self.controller = Controller()
                self.Handler = EventHandler(self.controller)
                sprites = pygame.sprite.Group()
                self.game_start(config_data, sprites)
                game_start = False

            if on_menus[0] or on_menus[1] or on_menus[2]:
                if on_menus[1] or on_menus[2]:
                    result_menu.draw_result_objects(self.screen, on_menus[1])
                else:
                    main_menu.draw_buttons(self.screen)

                # main_menu.draw_buttons(self.screen)
                for event in pygame.event.get():
                    if on_menus[0]:
                        main_menu.check_hover(event)
                        button_clicked = main_menu.check_button_click(event)
                        main_menu.draw_buttons(self.screen)
                        if button_clicked > -1:
                            game_modes[button_clicked] = True
                            on_menus[0] = False
                            game_start = True
                    
                    elif on_menus[1] or on_menus[2]:
                        result_menu.check_hover(event)
                        on_menus[0] = result_menu.check_back_main_menu(event)
                        result_menu.draw_result_objects(self.screen, on_menus[1])
                        if on_menus[0]:
                            on_menus[1] = False
                            on_menus[2] = False
            else:
                self.Handler.handle(pygame.event.get())
                # check if data collection mode is activated
                if (game_modes[1]):
                    data_collector.save_current_status(self.lander, self.surface, self.controller)
                self.screen.blit(background_image,(0,0))
                self.update_objects()
                # then update the visuals on screen from the list
                sprites.draw(self.screen)
                if (self.lander.landing_pad_collision(self.surface)):
                    on_menus[1] = True
                # check if lander collided with surface
                elif (self.lander.surface_collision(self.surface) or self.lander.window_collision((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))):
                    on_menus[2] = True
                
                if (on_menus[1] or on_menus[2]):
                    game_start = False
                    for i in range(len(game_modes)):
                        game_modes[i] = False


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
                        self.controller)
        self.game_logic.add_lander(lander)
        return lander

    def game_start(self, config_data, sprites):
        # Creates the lander object
        self.lander = self.setup_lander(config_data)
        self.surface = Surface((config_data['SCREEN_WIDTH'], config_data['SCREEN_HEIGHT']))
        sprites.add(self.lander)
        sprites.add(self.surface)
