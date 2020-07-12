import RPi.GPIO as GPIO
import time

all_pins = [5, 6, 13]
mid_pins = [5, 13]


def signal(ll):
    GPIO.setmode(GPIO.BCM)
    for pin in all_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    if ll == "off":
        for pin in all_pins:
            GPIO.output(pin, GPIO.LOW)
    if ll == "mid":
        for pin in all_pins:
            GPIO.output(pin, GPIO.LOW)

        for pin in mid_pins:
            GPIO.output(pin, GPIO.HIGH)
    if ll == "on":
        for pin in all_pins:
            GPIO.output(pin, GPIO.HIGH)


def initial():
    GPIO.setmode(GPIO.BCM)
    for pin in all_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


def final():
    GPIO.cleanup()

# initial()
# signal('on')
# time.sleep(3)
# signal('mid')
# time.sleep(3)
# signal('off')
# time.sleep(3)
# signal('mid')
# time.sleep(3)
# final()
