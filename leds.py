from machine import Pin
import time

led= Pin (12, Pin.OUT)
led.value(1)  # Encender led
time.sleep(1)
led.off()

led= Pin (13, Pin.OUT)
led.value(2)  # Encender led
time.sleep(2)
led.off()

led= Pin (18, Pin.OUT)
led.value(3)  # Encender led
time.sleep(3)
led.off()

led= Pin (19, Pin.OUT)
led.value(4)  # Encender led
time.sleep(4)
led.off()