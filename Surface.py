import pygame, random, math

class Surface(pygame.sprite.Sprite):

    def __init__(self, screen, screen_dimension, location):
        pygame.sprite.Sprite.__init__(self)
        
        # pygame.draw.rect(self.image, (255,0,0), [0,0,200,5])
        polygon_surface_points = self.random_ground(screen_dimension[1], screen_dimension[0], 8)
        
        self.image = pygame.Surface([screen_dimension[0], screen_dimension[1]])
        # self.image = screen
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        # ans = [(0, screen_dimension[1]-(screen_dimension[1]*.2)), (screen_dimension[0], screen_dimension[1]-(screen_dimension[1]*.2)), (screen_dimension[0], screen_dimension[1]), (0, screen_dimension[1])]
        # self.rect = pygame.draw.polygon(self.image, (0,0,0), [(0,500), (screen_dimension[0], 500), (screen_dimension[0], screen_dimension[1]), (0, screen_dimension[1])])        
        self.rect = pygame.draw.polygon(self.image, (0,0,0), polygon_surface_points)
        # self.rect = pygame.draw.rect(self.image, (0,0,0), [0,500,1000,1000])        
        self.rect = self.image.get_rect()
        # self.rect = pygame.draw.line(screen, (255,0,0), start_point, end_point, 5)
        # self.rect.x = start_point[0]
        # self.rect.y = start_point[1]

    def random_ground(self, screen_height, screen_width, spacing):
        screen_height = screen_height
        screen_width = screen_width
        # set out the boundaries
        highest_point = screen_height - (screen_height / 8)
        lowest_point = screen_height + screen_height
        left_most_point = 0
        right_most_point = screen_width + 1

        ans = [pygame.math.Vector2(left_most_point, highest_point)]

        # ans = [(1, 840), (1919, 840), (1919, 1079), (1, 1079)]
        # ans = [(0,400),(400,400), (400,600), (0,600)]
        ans = [(left_most_point, highest_point)]
        #ans = [(0, screen_height-(screen_height*.2)), (screen_width, screen_height-(screen_height*.2)), (screen_width, screen_height), (0, screen_height)]
        #ans = [(0, screen_height-(screen_height*.2)), (screen_width, screen_height-(screen_height*.2)), (screen_width, screen_height), (0, screen_height)]
        # ans = [(1, 100), (200,100), (200,840),(1,840)]
        number_of_points = screen_width / spacing
        i = 0
        while i < number_of_points:
            rand = random.random()
            rand = rand * 25
            print("Rand = " + str (rand))


            last_y_point = ans[i][1]
            last_x_point = ans[i][0]
            print("last y " + str(last_y_point))
            print("last x " + str(last_x_point))
            ans.append((last_x_point + spacing, highest_point + rand))
            i = i + 1

        ans.append((right_most_point, highest_point))
        ans.append((right_most_point ,lowest_point))
        ans.append((left_most_point, lowest_point))
        print(ans)


        return ans
