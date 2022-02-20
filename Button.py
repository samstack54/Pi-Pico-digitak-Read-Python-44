from machine import Pin
from utime import sleep

Button = Pin(14, Pin.IN)

while True:
    if Button.value() == 1:
        print("ON")
        sleep(0.5)
    else:
        print("OFF")
        sleep(0.5)

        
