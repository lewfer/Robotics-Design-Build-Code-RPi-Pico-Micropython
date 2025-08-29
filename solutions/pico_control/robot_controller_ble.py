from bleperipheral import blePeripheral
from machine import Pin
import time


forward = Pin(21, Pin.IN, Pin.PULL_DOWN) 
backward = Pin(20, Pin.IN, Pin.PULL_DOWN) 
left = Pin(19, Pin.IN, Pin.PULL_DOWN) 
right = Pin(18, Pin.IN, Pin.PULL_DOWN)

def setMessage():
    time.sleep(0.1)
    if left.value()==1:
        action = "L"
    elif right.value()==1:
        action = "R"
    elif forward.value()==1:
        action = "F"
    elif backward.value()==1:
        action = "B"
    else:
        action = "S"
    
    print(action)
    return action
    
ble = blePeripheral("Bob's Robot", setMessage)
ble.run()

