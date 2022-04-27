from dooby_motordriver import MotorDriver

class RobotMover(object):

    def __init__(self):
        self.motor_driver = MotorDriver()


    def cmd_vel_callback(self, msg):
        linear_speed = msg.linear.x
        angular_speed = msg.angular.z

        # Decide Speed
        self.motor_driver.set_cmd_vel(linear_speed, angular_speed)


if __name__ == '__main__':

    robot_mover = RobotMover()

    msg = ""

    msg.linear.x = 20
    msg.angular.z = 10
    
    robot_mover.cmd_vel_callback(msg)