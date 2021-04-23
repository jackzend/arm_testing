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
a = arm.Arm()
#time.sleep(1)
#a.current_position()
#a.move((512,512))
RANK_1 = (600, 512) # EXP DONE
RANK_2 = (610, 540) # EXP DONE
RANK_3 = (793, 556) # EXP DONE
RANK_4 = (833, 592) # EXP DONE
RANK_5 = (872, 626) # EXP DONE
RANK_6 = (914, 681) # EXP DONE
RANK_7 = (948, 743) # EXP DONE
RANK_8 = (979, 818) # EXP DONE


#while(True):
#    time.sleep(0.2)
#    print(a.current_position())



a.recenter()
g.release()
a.move((747,659))
time.sleep(1)
g.grip()
a.recenter()
a.move((642,760))
a.move((312,434))
g.release()
a.move((312,550))
a.recenter()









#a.move(RANK_3) 979 610
#a.move(RANK_2)
#a.move(RANK_1)
#a.move(RANK_3)
#a.move(RANK_1)
#a.move(RANK_2)
#a.move(RANK_1)
#a.recenter()





#time.sleep(0.2)
#print("End Pos (Elbow,Shoulder)")
#print(a.current_position())
#a.move((1023,646))
#a.move((512,512))
#a.move(RANK_A)
#a.move(RANK_D)
#a.move(RANK_B)
#a.move(RANK_C)
#a.move((600,500))
#a.move(RANK_H)

a.close()
g.close()
