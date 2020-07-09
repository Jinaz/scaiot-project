import time
import random
import numpy as np
from numpy import savetxt

import DataFiles.Constants as CTS
#from HTSensorFunctions import HT_Sensor as hts


def genDummy():
    humudity = random.uniform(0,100)
    temperature = random.uniform(-40, 40)
    return humudity, temperature

def looper():

    datacontainer = np.zeros((2,10))
    n = 0
    while True:
        #check for change
        file = open(CTS.TRIGGERPATH, "r")
        content = file.read(4)
        if content == "True":

            data0 = datacontainer[0,:]
            data1 = datacontainer[1,:]

            # save to csv file
            savetxt('DATA/hum.csv', data0, delimiter=',')
            savetxt('DATA/temp.csv', data1, delimiter=',')

            #new_filename = CTS.DATAFILENAME
            print("data written")
            time.sleep(1)
        #uncomment to use sensor data
        #hum, temp = hts.getHTData()

        #dummy data
        hum,temp = genDummy()



        datacontainer[0][n] = hum
        datacontainer[1][n] = temp
        #,datetime.now().strftime("%Y%m%d%H%M%S"))
        n+=1
        time.sleep(1)

        #every 10 reset
        if n % 10 == 0:
            n = 0
            print(datacontainer)

def main_On_Py():
    looper()