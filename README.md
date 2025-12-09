# EJEMPLOS
##Leds.py
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

##analog.py
from machine import ADC, Pin
import time
POT_PIN=36 # Pin del potenciómetro

pot=Pin (POT_PIN) # Configurar pin del potenciómetro
adc_pot= ADC (pot) # Configurar ADC para el potenciómetro
adc_pot.width (ADC.WIDTH_12BIT) # Configurar resolución a 12 bits
adc_pot.atten (ADC.ATTN_11DB) # Configurar atenuación a 11dB para rango completo

while True:
    valor_pot= adc_pot.read() # Leer valor del potenciómetro
    print(f"Valor del potenciómetro: {valor_pot}") # Imprimir valor leído
    time.sleep(0.1) # Esperar 100 ms antes de la siguiente lectura

    ##libromotor.py
    from machine import Pin

#Motor 1
motor1_pin_a= Pin (12, Pin.OUT) # Configurar pin del motor como salida
motor1_pin_b= Pin (13, Pin.OUT) # Configurar pin del motor como salida
#Motor 2
motor2_pin_a= Pin (18, Pin.OUT) # Configurar pin del motor como salida
motor2_pin_b= Pin (19, Pin.OUT) # Configurar pin del motor como salida


def carro_adelante():
    motor1_pin_a.on()  # Encender motor 1 pin A
    motor1_pin_b.off() # Apagar motor 1 pin B
    motor2_pin_a.on()  # Encender motor 2 pin A
    motor2_pin_b.off() # Apagar motor 2 pin B

def carro_atrás():
    motor1_pin_a.off()  # Encender motor 1 pin A
    motor1_pin_b.on() # Apagar motor 1 pin B
    motor2_pin_a.off()  # Encender motor 2 pin A
    motor2_pin_b.on() # Apagar motor 2 pin B

def carro_detenerse():
    motor1_pin_a.off()  # Encender motor 1 pin A
    motor1_pin_b.off() # Apagar motor 1 pin B
    motor2_pin_a.off()  # Encender motor 2 pin A
    motor2_pin_b.off() # Apagar motor 2 pin B

def carro_izquierda():
    motor1_pin_a.off()  # Encender motor 1 pin A
    motor1_pin_b.on() # Apagar motor 1 pin B
    motor2_pin_a.on()  # Encender motor 2 pin A
    motor2_pin_b.off() # Apagar motor 2 pin B

def carro_derecha():
    motor1_pin_a.on()  # Encender motor 1 pin A
    motor1_pin_b.off() # Apagar motor 1 pin B
    motor2_pin_a.off()  # Encender motor 2 pin A
    motor2_pin_b.on() # Apagar motor 2 pin B

    ##motor.py
    from machine import Pin
import time

from libmotor import carro_adelante, carro_atrás, carro_detenerse, carro_izquierda, carro_derecha

#LLAMAR FUNCIONES
carro_adelante()
time.sleep(2)

carro_atrás()
time.sleep(2)

carro_detenerse()
time.sleep(2)

carro_izquierda()
time.sleep(2)

carro_derecha()
time.sleep(2)

##oled.py
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
oled.show()  # Actualizar pantalla para mostrar el textoç

##rgbneopixel.py
import machine
import time
import neopixel
PIN = 4  # Pin donde está conectado el NeoPixel
NUM_PIX = 3  # Número de LEDs NeoPixel
np=neopixel.NeoPixel(machine.Pin(PIN), NUM_PIX)
np[0]=(255,255,255)  # LED 1 en rojo
np[1]=(0,255,0)      # LED 2 en verde
np[2]=(0,0,255)      # LED 3 en azul
np.write()
