from blecentral import bleCentral
import PicoRobotics
from time import sleep
from machine import Pin

# LED for indicator
led = Pin("LED", Pin.OUT)

# Create robotics object
robot = PicoRobotics.KitronikPicoRobotics()
speed = 100

def flashLed():
    led.on()
    sleep(0.2)
    led.off() 
    sleep(0.2)
        
def receivedMessage(message):
    print(message)
    
    # Handle BLE messages
    if message == "#FOUND":
        flashLed()
    elif message == "#CONNECTED":
        flashLed()
    elif message == "#READY":
        flashLed()
    
    # Handle controller messages
    if message == "F":
        robot.motorOn(1, "f", speed)
        robot.motorOn(2, "f", speed)
    elif message == "B":
        robot.motorOn(1, "r", speed)
        robot.motorOn(2, "r", speed)
    elif message == "L":
        robot.motorOn(1, "f", 0)
        robot.motorOn(2, "f", speed)
    elif message == "R":
        robot.motorOn(1, "f", speed)
        robot.motorOn(2, "f", 0)
    elif message == "S":
        robot.motorOff(1)
        robot.motorOff(2)

flashLed()
ble = bleCentral("Bob's Robot", receivedMessage)
flashLed()
ble.run()
