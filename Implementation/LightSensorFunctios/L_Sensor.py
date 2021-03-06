#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import DataFiles.Constants as con

GPIO.setmode(GPIO.BCM)

def rc_time(pin_to_circuit=4):
    GPIO.setmode(GPIO.BCM)

    count = 0

    # Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    # Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    #GPIO.cleanup()

    ct = round(count / con.LIGHTRESIST)

    return count


def getLightData():
    return rc_time()