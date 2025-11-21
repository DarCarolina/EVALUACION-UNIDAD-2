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