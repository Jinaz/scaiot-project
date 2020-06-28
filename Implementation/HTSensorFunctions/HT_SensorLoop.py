import time
import os
from datetime import datetime
import random

import HTSensorFunctions.Constants as CTS
#from HTSensorFunctions import HT_Sensor as hts
def genDummy():
    humudity = random.uniform(0,100)
    temperature = random.uniform(-40, 40)
    return humudity, temperature

def looper():
    notfirst = False
    filename = CTS.DATAFILENAME
    new_filename = ""

    datacontainer = [None] * 10
    n = 0
    while True:
        #check for change
        file = open(CTS.TRIGGERPATH, "r")
        content = file.read(4)
        if content == "True":
            if notfirst:
                os.remove(filename)
                print(filename, " Removed!")
                filename = new_filename
            filename = filename.format(n)
            notfirst = True
            file = open(filename, "w")
            file.write(str(datacontainer))
            file.close()
            new_filename = CTS.DATAFILENAME
            print("data written")
            time.sleep(1)
        #uncomment to use sensor data
        #hum, temp = hts.getHTData()

        #dummy data
        hum,temp = genDummy()
        datacontainer[n] = (hum,temp,datetime.now().strftime("%Y%m%d%H%M%S"))
        n+=1
        time.sleep(1)

        #every 10 reset
        if n % 10 == 0:
            n = 0
            print(datacontainer)

looper()