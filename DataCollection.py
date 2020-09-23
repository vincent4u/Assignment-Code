
class DataCollection:

    def __int__(self):
        self.distance_to_target = []
        self.distance_to_ground = []
        self.velocity = []

    def add_row(self, distance_to_target, distance_to_ground, velocity):
        self.distance_to_target.append(distance_to_target)
        self.distance_to_ground.append(distance_to_ground)
        self.velocity.append(velocity)

    def get_distance_to_target(self):
        return self.distance_to_target

    def get_distance_to_ground(self):
        return self.distance_to_ground

    def get_velocity(self):
        return self.velocity