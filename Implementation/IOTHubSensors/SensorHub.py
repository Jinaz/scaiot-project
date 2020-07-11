import DataFiles.Constants as CTS
from HTSensorFunctions import HT_Sensor as hts
import LightSensorFunctios.L_Sensor as ls
import random


def genIRDummy():
    ir = random.uniform(0, 80)
    return ir


def getData():
    humidity, temperature = hts.getHTData()
    lightlevel = ls.getLightData()
    ir_value = genIRDummy()

    return humidity, temperature, lightlevel, ir_value
