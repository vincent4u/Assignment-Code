import pygame
from Vector import Vector
from CollisionUtility import CollisionUtility


class Lander(pygame.sprite.Sprite):

    def __init__(self, filepath, location, velocity, controller):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filepath)
        self.original_image = self.image
        # self.image = pygame.transform.scale(self.image, (1, 1))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.velocity = velocity
        self.position = Vector(location[0], location[1])
        self.controller = controller
        self.gravity = Vector(0, 0.5)
        self.current_angle = 0

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.original_image, angle)

    def landing_pad_collision(self, surface):
        return self.rect.colliderect(surface.landing_pad)
            
    def surface_collision(self, surface):
        if (self.rect.colliderect(surface.polygon_rect)):
            print("POSSIBLE COLLISION")
            collided = CollisionUtility.check_lander_collision_with_surface(self, surface)
            return collided
    
    def window_collision(self, screen_dimensions):
        return CollisionUtility.check_gameobject_window_collision(self, screen_dimensions)

    def update_lander(self, delta_time):
        # update the changes in velocity
        # delta time needs to be in seconds not milliseconds
        # collect the movement information from the Controller
        movement = Vector(0, 0)
        theta = 0.0

        if self.controller.is_up():
            movement = movement.add(Vector(0, -1)).scalar_multiply(delta_time)

        if self.controller.is_left():
            theta = 20 * delta_time

        if self.controller.is_right():
            theta = -20 * delta_time

        self.current_angle = self.current_angle + theta

        movement = movement.rotate(-self.current_angle)

        if self.velocity.x > 0:
            air_resistance = Vector(-0.2, 0)
        else:
            air_resistance = Vector(0.2, 0)

        last_velocity = Vector(self.velocity.x, self.velocity.y)

        air_resistance = air_resistance.scalar_multiply(delta_time)
        gravity = self.gravity.scalar_multiply(delta_time)
        self.velocity = self.velocity.add(air_resistance).add(gravity).add(movement)

        speed = self.velocity.length()
        if speed > 8:
            self.velocity = last_velocity
        """
        print("Velocity: ")
        self.velocity.print()
        print("Position: ")
        self.position.print()
        print("Current Angle: ")
        print(self.current_angle)
        print("================ \n")
        """

        # update the changes in position
        self.position = self.position.add(self.velocity)
        location = [self.position.x, self.position.y]
        self.rect.left, self.rect.top = location
        self.rotate(self.current_angle)

    def check_boundary(self, screen_size):
        screen_width = screen_size[0]
        screen_height = screen_size[1]
