import RPi.GPIO as GPIO
import time

def openWindow():
    servoPIN = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 als PWM mit 50Hz
    p.start(2.5)  # Initialisierung

    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)

    p.stop()
    #GPIO.cleanup()


def closeWindow():
    servoPIN = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 als PWM mit 50Hz
    p.start(7.5)  # Initialisierung

    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)

    p.stop()
    #GPIO.cleanup()
