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
            movement = movement.add(Vector(0, -2.1))

        if self.controller.is_left():
            movement = movement.add(Vector(-1, 0))

        if self.controller.is_right():
            movement = movement.add(Vector(1, 0))



        self.velocity = self.velocity.scalar_multiply(delta_time).add(self.gravity).add(movement)

        print(str(self.velocity.x) + " " + str(self.velocity.y))

        # update the changes in position
        self.position = self.position.add(self.velocity)
        location = [self.position.x, self.position.y]
        self.rect.left, self.rect.top = location
