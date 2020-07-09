import time
import random
import numpy as np
from numpy import savetxt

import DataFiles.Constants as CTS
#from HTSensorFunctions import HT_Sensor as hts
import LightSensorFunctios.L_Sensor as ls


def genHTDummy():
    humudity = random.uniform(0,100)
    temperature = random.uniform(-40, 40)
    return humudity, temperature

def genLDummy():
    light = random.uniform(0,100)
    return light

def genIRDummy():
    ir = random.uniform(0,80)
    return ir

def looper():

    datacontainer = np.zeros((4,10))
    n = 0
    while True:
        #check for change
        file = open(CTS.TRIGGERPATH, "r")
        content = file.read(4)
        if content == "True":

            data0 = datacontainer[0,:]
            data1 = datacontainer[1,:]
            data2 = datacontainer[2,:]
            data3 = datacontainer[3,:]

            # save to csv file
            savetxt('DATA/hum.csv', data0, delimiter=',')
            savetxt('DATA/temp.csv', data1, delimiter=',')
            savetxt('DATA/light.csv', data2, delimiter=',')
            savetxt('DATA/ir_data.csv', data3, delimiter=',')

            #new_filename = CTS.DATAFILENAME
            print("data written")
            time.sleep(1)
        #uncomment to use sensor data
        #hum, temp = hts.getHTData()
        #light = ls.getLightData()

        #dummy data
        hum,temp = genHTDummy()
        light = genLDummy()
        ir = genIRDummy()

        datacontainer[0][n] = hum
        datacontainer[1][n] = temp
        datacontainer[2][n] = light
        datacontainer[3][n] = ir
        #,datetime.now().strftime("%Y%m%d%H%M%S"))
        n+=1
        time.sleep(1)

        #every 10 reset
        if n % 10 == 0:
            n = 0
            print(datacontainer)

def main_On_Py():
    looper()