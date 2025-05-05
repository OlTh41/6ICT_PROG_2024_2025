import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

GPIO.output(7, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def aan(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def uit(self):
        GPIO.output(self.pin, GPIO.LOW)

led_5 = Led(5)
led_21 = Led(21)

while True:
    led_5.aan()
    led_21.uit()
    time.sleep(1)

    led_5.uit()
    led_21.aan()
    time.sleep(1)


