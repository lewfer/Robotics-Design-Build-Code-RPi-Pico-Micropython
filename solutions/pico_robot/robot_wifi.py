from PicoRobotics import KitronikPicoRobotics
import time
from net import Wifi
from machine import Pin
from time import sleep

PORT = 5000

# LED for indicator
led = Pin("LED", Pin.OUT)

# Create robotics object
motor = KitronikPicoRobotics()

def flashLed():
    led.on()
    sleep(0.2)
    led.off() 
    sleep(0.2)
    
# Create a network object
wifi = Wifi()
flashLed()
    
    
try:
    # Connect to WIFI
    wifi.connect()
    flashLed()
    
    # Create receiver to listen for messages
    wifi.createReceiver(PORT)
    flashLed()

    # Receive messages
    while True:
        message = wifi.receiveMessage()
        print("Received", message)

        # Process the message, which could be a command like "stop" or "forward,20"
        # The message is split into two parts if there is a comma
        splitMessage = message.strip().split(",")

        # First part of message is the command
        action = splitMessage[0]

        # Carry out command
        if action=="forward":
            speed = int(splitMessage[1])
            motor.motorOn(1, "f", speed)
            motor.motorOn(2, "f", speed)
        elif action=="backward":
            speed = int(splitMessage[1])
            motor.motorOn(1, "r", speed)
            motor.motorOn(2, "r", speed)
        elif action=="left":
            speed = int(splitMessage[1])
            motor.motorOn(1, "r", speed)
            motor.motorOn(2, "f", speed)
        elif action=="right":
            speed = int(splitMessage[1])
            motor.motorOn(1, "f", speed)
            motor.motorOn(2, "r", speed)            
        elif action=="stop":
            motor.motorOff(1)
            motor.motorOff(2)
        elif action=="servoup":
            motor.servoWrite(1, 160)
        elif action=="servodown":
            motor.servoWrite(1, 20)
except Exception as e:
    print("Error", e)
    


