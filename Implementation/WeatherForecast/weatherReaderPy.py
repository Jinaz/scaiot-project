import urllib.request, json
import numpy as np

def readurl():
    url = "https://sciot-weather-forecast.azurewebsites.net/api/WeatherForecast"
    with urllib.request.urlopen(url) as dat:
        data = json.loads(dat.read().decode())
        #print(data)

        #print(data[0]["temp"])
        #print(data[0]["snow"])
        #print(data[0]["weather"]["description"])

        we = 0

        if "cloud" in data[0]["weather"]["description"]:
            we = 1
        elif "rain" in data[0]["weather"]["description"] or "rain" in data[1]["weather"]["description"]:
            we = 2
        if data[0]["snow"] > 0 or data[1]["snow"]:
            we = 3

        meantemp = np.mean(np.array([data[0]["temp"], data[1]["temp"]]))
        return int(np.round(meantemp)), we
