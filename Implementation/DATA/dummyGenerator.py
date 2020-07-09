# save numpy array as csv file
from numpy import asarray
from numpy import savetxt

def genDummyTemp():
    # define data
    data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
    # save to csv file
    savetxt('temp.csv', data, delimiter=',')

def genDummyHum():
    # define data
    data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
    # save to csv file
    savetxt('hum.csv', data, delimiter=',')

def genDummyLight():
    # define data
    data = asarray([[15, 10, 20, 30, 40, 50, 60, 70, 80, 90]])
    # save to csv file
    savetxt('light.csv', data, delimiter=',')

def genDummyIR():
    # define data
    data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
    # save to csv file
    savetxt('ir_data.csv', data, delimiter=',')

def genAllDummy():
    genDummyHum()
    genDummyTemp()
    genDummyIR()
    genDummyLight()

def generateDummy():
    genAllDummy()