# Template to control a RPi Pico robot over Wifi from another Pico using a 2-axis analogue joystick

import time
from machine import ADC, Pin
from net import Wifi 

# Specify the IP address of your robot
HOST = "192.168.1.239" 

# Specify the port number to send messages on
PORT = 5000

#  Set up axes on pins 27 and 28 as an analogue input pin
axisy = ADC(27)
axisx = ADC(28)

# Set up the button on pin 18 as a digital input pin
press = Pin(18, Pin.IN, Pin.PULL_UP)

# Create a network object
wifi =  Wifi()

try:
    # Connect to WIFI
    wifi.connect()

    # Create receiver to listen for messages
    wifi.createSender(HOST, PORT)

    # Receive messages
    while True:
        # Centre x and y on 0
        valy = axisy.read_u16() - 32767
        valx = axisx.read_u16() - 32767

        # Act on the values
        print(valx,valy, press.value())
        if valy > 2000:
            wifi.sendMessage("forward,20")
        else:
            wifi.sendMessage("stop")
        time.sleep(0.1)

except Exception as e:
    print("Error", e)
