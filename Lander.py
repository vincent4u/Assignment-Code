import pygame
from Vector import Vector


class Lander(pygame.sprite.Sprite):

    def __init__(self, filepath, location, velocity, controller):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.velocity = velocity
        self.position = Vector(location[0], location[1])
        self.controller = controller
        self.gravity = Vector(0, 1)

    def update_lander(self, delta_time):
        # update the changes in velocity
        # delta time needs to be in seconds not milliseconds
        # collect the movement information from the Controller
        movement = Vector(0, 0)

        if self.controller.is_up():
            movement = movement.add(Vector(0, -3.1)).scalar_multiply(delta_time)

        if self.controller.is_left():
            movement = movement.add(Vector(-1, 0)).scalar_multiply(delta_time)

        if self.controller.is_right():
            movement = movement.add(Vector(1, 0)).scalar_multiply(delta_time)

        if self.velocity.x > 0:
            air_resistance = Vector(-0.2, 0)
        else:
            air_resistance = Vector(0.2, 0)

        last_velocity = Vector(self.velocity.x,self.velocity.y)

        air_resistance = air_resistance.scalar_multiply(delta_time)
        gravity = self.gravity.scalar_multiply(delta_time)
        self.velocity = self.velocity.add(air_resistance).add(gravity).add(movement)

        speed = self.velocity.length()
        if speed > 8:
            self.velocity = last_velocity

        # update the changes in position
        self.position = self.position.add(self.velocity)
        location = [self.position.x, self.position.y]
        self.rect.left, self.rect.top = location
