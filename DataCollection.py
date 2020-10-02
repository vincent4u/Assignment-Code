
class DataCollection:

    def __int__(self):
        self.data_file = open("ce889_dataCollection.csv", "a")
        self.data_file.close()

    def save_current_status(self, lander, surface, controller):
        # open file
        self.data_file = open("ce889_dataCollection.csv", "a")
        
        # inputs
        current_velocity = lander.velocity
        current_speed = current_velocity.length()
        if (lander.is_going_down):
            current_speed = (-1)*current_speed
        current_angle = lander.current_angle
        x_target = surface.centre_landing_pad[0] - lander.position.x
        y_target = surface.centre_landing_pad[1] - lander.position.y
        dist_to_surface = surface.polygon_rect.topleft[1] - lander.position.y

        # outputs
        thrust = 0
        turning = 0
        if (controller.is_up()):
            thrust = 1
        if (controller.is_left()):
            turning = -1
        elif (controller.is_right()):
            turning = 1

        # create comma separated string row
        status_row = str(current_speed)+"," + \
                    str(current_angle) + "," + \
                    str(x_target) + "," + \
                    str(y_target) + "," + \
                    str(dist_to_surface) + "," + \
                    str(thrust) + "," + \
                    str(turning) + "\n"
        # print(status_row)
        
        # save comma separated row in the file
        self.data_file.write(status_row)
        self.data_file.close()