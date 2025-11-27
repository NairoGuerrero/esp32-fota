# main_v2.py
import time
from machine import Pin

led = Pin(2, Pin.OUT)

print("Iniciando main.py v2 (ACTUALIZADO)")

while True:
    print("hola nairo v2 - OTA OK")
    led.value(1)
    time.sleep(1)
    print("hola nairo v2 - OTA OK")
    led.value(0)
    time.sleep(1)
