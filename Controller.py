

class Controller:
    up = False
    left = False
    right = False

    def __init__(self):
        self

    def set_up(self, action):
        self.up = action

    def is_up(self):
        return self.up

    def set_right(self, action):
        self.right = action

    def is_right(self):
        return self.right

    def set_left(self, action):
        self.left = action

    def is_left(self, action):
        return self.left
