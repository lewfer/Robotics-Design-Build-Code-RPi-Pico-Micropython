from PicoRobotics import KitronikPicoRobotics
import time
from net import Wifi

PORT = 5000

# Create robotics object
motor = KitronikPicoRobotics()

# Create a network object
wifi = Wifi()

try:
    # Connect to WIFI
    wifi.connect()

    # Create receiver to listen for messages
    wifi.createReceiver(PORT)

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
            # Forward command has a second part, which is the speed
            speed = int(splitMessage[1])
            motor.motorOn(1, "f", speed)
            motor.motorOn(2, "f", speed)
        elif action=="stop":
            motor.motorOff(1)
            motor.motorOff(2)


except Exception as e:
    print("Error", e)