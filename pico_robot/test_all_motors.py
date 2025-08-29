# AllMotorTest.py
# Test code that ramps each motor speed from 0-100 then changes direction and does it again.


import PicoRobotics
import time

board = PicoRobotics.KitronikPicoRobotics()
directions = ["f","r"]


for direction in directions:
    for speed in range(0,100):
        board.motorOn(1, direction, speed)
        board.motorOn(2, direction, speed)
        board.motorOn(3, direction, speed)
        board.motorOn(4, direction, speed)
        time.sleep(0.1) 
        
board.motorOff(1)
board.motorOff(2)
board.motorOff(3)
board.motorOff(4)