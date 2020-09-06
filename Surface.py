import pygame, random, math

class Surface(pygame.sprite.Sprite):

    def __init__(self, screen, screen_dimension, location):
        pygame.sprite.Sprite.__init__(self)
        # create the points for the polygon 
        polygon_surface_points = self.random_ground(screen_dimension[1], screen_dimension[0], 8)
        # create the canvas where the polygon will be painted, make it 
        self.image = pygame.Surface([screen_dimension[0], screen_dimension[1]])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        # create the polygon using the random points
        pygame.draw.polygon(self.image, (0,0,0), polygon_surface_points)        

        self.rect = self.image.get_rect()

    def random_ground(self, screen_height, screen_width, spacing):
        screen_height = screen_height
        screen_width = screen_width

        # set out the boundaries
        highest_point = screen_height - (screen_height / 8)
        lowest_point = screen_height + screen_height
        left_most_point = 0
        right_most_point = screen_width + 1
        ans = [(left_most_point, highest_point)]
        number_of_points = screen_width / spacing
        i = 0

        while i < number_of_points:
            rand = random.random()
            rand = rand * 25
            last_y_point = ans[i][1]
            last_x_point = ans[i][0]
            ans.append((last_x_point + spacing, highest_point + rand))
            i = i + 1

        ans.append((right_most_point, highest_point))
        ans.append((right_most_point, lowest_point))
        ans.append((left_most_point, lowest_point))
        return ans
