import Adafruit_DHT as dht
import time

def readHumTemp(timeSeconds):
    #log data into an array
    hum = []
    temp = []

    #define sensor and the pin used to get data
    sensor = dht.DHT11
    gpio = 17

    #log for timeSeconds samples
    for i in range(timeSeconds):
        humidity, temperature = dht.read_retry(sensor, gpio)
        time.sleep(1)
        hum.append(humidity)
        temp.append(temperature)

    return hum, temp

def getHTData(sensor = dht.DHT11,gpio = 17):
    humidity, temperature = dht.read_retry(sensor, gpio)
    return humidity,temperature

