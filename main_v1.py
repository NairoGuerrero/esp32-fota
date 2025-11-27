# main_v1.py
import time
from machine import Pin

led = Pin(2, Pin.OUT)  # GPIO2

print("Iniciando main.py v1")

while True:
    print("hola nairo v1")
    led.value(1)
    time.sleep(3)
    print("hola nairo v1")
    led.value(0)
    time.sleep(3)
