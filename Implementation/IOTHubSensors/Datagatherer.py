import DataFiles.Constants as cs
import csv
import re
import numpy as np

def readData():
    i = 0
    data_out = []
    for file in cs.DATAFILENAMES:
        mostRecentvalue = None
        with open(file, newline='') as csvfile:
            dataReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in dataReader:
                data = re.split(',+',row[0])
                for n in range(len(data)):
                   data[n] = float(data[n])
                mostRecentvalue = np.mean(data)
        data_out.append(mostRecentvalue)
        i+=1
    return data_out

