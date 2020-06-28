# Sensor
We use the DHT11 and the Adafriut library

# Coding
The programming language will be python.
The code to take the data is according to the following tutorial:
https://tutorials-raspberrypi.de/raspberry-pi-luftfeuchtigkeit-temperatur-messen-dht11-dht22/

# Data Storage

Dataformat is a str which can be converted to float. If empty it is a None object.

Using csv or plain text files the data can be stored.

At the moment: 10 samples are stored with timestamps

Humidity, Temperature, Time[year,month,day,hour,minute,second]

