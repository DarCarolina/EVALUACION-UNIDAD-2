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