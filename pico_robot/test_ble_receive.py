# Test receiving BLE messages as a central

from blecentral import bleCentral


def receivedMessage(message):
   print("Recieved ", message)
     
ble = bleCentral("my peripheral", receivedMessage)
ble.run()
