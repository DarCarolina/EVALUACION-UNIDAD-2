# EJEMPLOS
## analog.py
    Este programa lee el valor de un potenciómetro conectado al pin 36 del ESP32 usando el convertidor ADC (Análogo-Digital) y muestra los valores en pantalla de forma continua.

    Paso a paso:

    Define el pin 36 como entrada del potenciómetro.

    Configura el ADC con:

    12 bits de resolución → valores entre 0 y 4095.

    Atenuación 11dB → permite medir voltajes desde ~0V hasta ~3.3V.

    En un bucle infinito (while True):

    Lee el valor del potenciómetro con adc_pot.read().

## leds.py
    Tu programa controla cuatro pines (12, 13, 18 y 19) de un microcontrolador compatible con MicroPython (por ejemplo ESP32).
    En cada pin conecta un LED y lo enciende durante un tiempo distinto, uno tras otro.

    El flujo es:

    Configura el pin 12 como salida → enciende el LED → espera 1 segundo → lo apaga.

    Configura el pin 13 como salida → enciende el LED → espera 2 segundos → lo apaga.

    Configura el pin 18 como salida → enciende el LED → espera 3 segundos → lo apaga.

    Configura el pin 19 como salida → enciende el LED → espera 4 segundos → lo apaga.

## libmotor.py
    El programa controla dos motores DC, cada uno con dos pines:

    Motor 1: pines 12 y 13

    Motor 2: pines 18 y 19

    Cada motor puede girar hacia adelante o hacia atrás dependiendo de cuál pin está encendido (HIGH) y cuál está apagado (LOW).

    Con esto creas funciones para mover un carro robot:

        Adelante

        Atrás

        Izquierda

        Derecha

        Detenerse

## motor.py
    Este programa importa las funciones que controlan los motores desde el archivo libmotor.py y luego las ejecuta una por una, cada una durante 2 segundos.

    Básicamente, el carro robot:

        Avanza 2 segundos

        Retrocede 2 segundos

        Se detiene 2 segundos

        Gira a la izquierda 2 segundos

        Gira a la derecha 2 segundos

    Y luego termina la ejecución.

## oled.py
    Este programa:

    Configura el bus I2C del ESP32.

    Escanea dispositivos conectados al bus.

    Inicializa una pantalla OLED 128×64 con el controlador SSD1306.

    Limpia la pantalla.

    Muestra dos líneas de texto:

    Hola, Mundo!

    :3

    Actualiza la pantalla para que el texto aparezca.

## rgbneopixel.py
    Este programa controla una tira (o anillo) de 3 LEDs NeoPixel conectados al pin 4, y les asigna diferentes colores:

    LED 1 → Blanco (255,255,255)

    LED 2 → Verde (0,255,0)

    LED 3 → Azul (0,0,255)

    Luego actualiza los LEDs para mostrar esos colores.
