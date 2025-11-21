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

