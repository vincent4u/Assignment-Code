
class DataCollection:

    def __init__(self):
        self.data_file = open("ce889_dataCollection.csv", "a")
        self.data_file.close()

    def get_input_row(self, lander, surface, controller):
        # inputs
        current_velocity = lander.velocity
        current_speed = current_velocity.length()
        # if (lander.is_going_down):
        #     current_speed = (-1)*current_speed
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
        input_row = str(current_speed)+"," + \
                    str(current_velocity.x) + "," + \
                    str(current_velocity.y) + "," + \
                    str(current_angle) + "," + \
                    str(x_target) + "," + \
                    str(y_target) + "," + \
                    str(dist_to_surface)

        return input_row

    def save_current_status(self, lander, surface, controller):
        # open file
        self.data_file = open("ce889_dataCollection.csv", "a")
        
        input_row = self.get_input_row(lander, surface, controller)

        # add output values to the string input row
        status_row = input_row + "," + \
                    str(thrust) + "," + \
                    str(turning[0]) + "," + str(turning[1]) + "\n"
        
        # save comma separated row in the file
        self.data_file.write(status_row)
        self.data_file.close()