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