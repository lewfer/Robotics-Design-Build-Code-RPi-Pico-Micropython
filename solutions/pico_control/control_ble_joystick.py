from bleperipheral import blePeripheral
from machine import ADC, Pin
from time import sleep

# LED for indicator
led = Pin("LED", Pin.OUT)

#  Set up axes on pins 27 and 28 as an analogue input pin
axisy = ADC(27)
axisx = ADC(28)


forward = Pin(21, Pin.IN, Pin.PULL_DOWN) 
backward = Pin(20, Pin.IN, Pin.PULL_DOWN) 
left = Pin(19, Pin.IN, Pin.PULL_DOWN) 
right = Pin(18, Pin.IN, Pin.PULL_DOWN)

def flashLed():
    led.on()
    sleep(0.2)
    led.off() 
    sleep(0.2)
    
    
def setMessage():
    sleep(0.1)
    # Centre x and y on 0
    valy = axisy.read_u16() - 32767
    valx = axisx.read_u16() - 32767
    
    print(valx, valy)

    
    if valx<-500:
        action = "L"
    elif valx>500:
        action = "R"
    elif valy>500:
        action = "F"
    elif valy<-500:
        action = "B"
    else:
        action = "S"
    
    print(action)
    return action

flashLed()
ble = blePeripheral("Bob's Robot", setMessage)
flashLed()
ble.run()




