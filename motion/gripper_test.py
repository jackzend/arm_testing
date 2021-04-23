from pypose.driver import Driver
from pypose.ax12 import P_MOVING, P_GOAL_SPEED_L

import arm
import gripper
import time

driver = Driver(port='/dev/tty.usbserial-AR0JW21B')

# Import AX-12 register constants


# Get "moving" register for servo with ID 1
#is_moving = driver.getReg(1, P_MOVING, 1)

# Set the "moving speed" register for servo with ID 1
#speed = 50 # A number between 0 and 1023
#driver.setReg(1, P_GOAL_SPEED_L, [speed%256, speed>>8])
#driver.setReg(2,P_GOAL_SPEED_L, [speed%256, speed>>8])

g = gripper.Gripper()

g.move(512)

g.close()

