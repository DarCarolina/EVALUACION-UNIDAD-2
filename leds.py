from machine import Pin
led= Pin (12, Pin.OUT)
led.value(1)  # Encender led
led.off()

led= Pin (13, Pin.OUT)
led.value(2)  # Encender led
led.off()

led= Pin (18, Pin.OUT)
led.value(3)  # Encender led
led.off()

led= Pin (19, Pin.OUT)
led.value(4)  # Encender led
led.on()