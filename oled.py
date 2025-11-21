from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import time

# Configurar I2C
i2c= I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

#Mostrar dispositivos I2C detectados
print("Dispositivos I2C detectados:", i2c.scan())

#Inicializar pantalla OLED 128x64
ancho=128
alto=64
oled= SSD1306_I2C(ancho, alto, i2c)

#Mostrar texto en la pantalla OLED
oled.fill(0)  # Limpiar pantalla
oled.text("Hola, Mundo!", 0, 0)  # Mostrar texto en la posición (0,0)
oled.text(":3",0,16)
oled.show()  # Actualizar pantalla para mostrar el texto

