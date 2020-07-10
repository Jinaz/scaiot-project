import RPi.GPIO as GPIO
import time

def signal(ll):
    pin = 16
    if ll == "off":
        pin = 29
    if ll == "mid":
        pin = 31
    if ll == "on":
        pin = 33

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

    GPIO.output(pin, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)

    GPIO.cleanup()

