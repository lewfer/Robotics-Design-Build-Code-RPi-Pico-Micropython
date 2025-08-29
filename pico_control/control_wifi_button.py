# Template to control a RPi Pico robot over Wifi from another Pico using buttons as controls

import time
from machine import Pin
from net import Wifi 

# Specify the IP address of your robot
HOST = "192.168.1.239" 

# Specify the port number to send messages on
PORT = 5000

# Set up a button on pin 16 as a digital input pin
up = Pin(18, Pin.IN, Pin.PULL_DOWN) 

# Create a wifi object
wifi =  Wifi()

try:
    # Connect to WIFI
    wifi.connect()

    # Set up a message sender
    wifi.createSender(HOST, PORT)

    # Send messages
    while True:
        if up.value()==1:
            message = "forward,20"
        else:
            message = "stop"
            
        print(message)
        wifi.sendMessage(message)
        time.sleep(0.1)

except Exception as e:
    print("Error", e)
