import RPi.GPIO as GPIO

from time import sleep

BIN_NUM = {0: 31, 1: 33, 2: 35, 3: 37}  # map digit to gpio pins

RANK_NUM = {"h":[0,0,0,0],"g":[0,0,0,1],"f":[0,0,1,0],"e":[0,0,1,1],"d":[0,1,0,0],"c":[0,1,0,1],"b":[0,1,1,0],
           "a":[0,1,1,1],"ob1":[1,0,0,0], "ob2":[1,0,0,1], "ob3":[1,0,1,0], "ob4":[1,0,1,1], "r1":[1,1,0,0],
            "r2":[1,1,0,1], "r3":[1,1,1,0], "r4":[1,1,1,1],}

OUTPUT = {0:GPIO.LOW, 1:GPIO.HIGH}
GPIO.setmode(GPIO.BOARD)

for key in BIN_NUM.keys():
    GPIO.setup(BIN_NUM[key], GPIO.OUT)


def go_to_rank(rank): # rank is a str
    temp_list = RANK_NUM[rank]

    for i in range(0, len(temp_list)):
        GPIO.output(BIN_NUM[i], OUTPUT[temp_list[i]])


go_to_rank("r1")
sleep(3)
go_to_rank("h")
sleep(3)
go_to_rank("g")
sleep(3)
go_to_rank("c")
sleep(3)
go_to_rank("r1")

GPIO.cleanup()


