# Test line following sensors (3 way) on a RPi Pico

from machine import Pin
import time

# Set up the sensors on the 3 pins
right = Pin(10, Pin.IN, Pin.PULL_DOWN) 
right = Pin(11, Pin.IN, Pin.PULL_DOWN) 
right = Pin(12, Pin.IN, Pin.PULL_DOWN) 

# Show the sensor status (True is light, False is dark)
while True:
    print(left.value(), middle.value(), right.value())
    time.sleep(0.01)