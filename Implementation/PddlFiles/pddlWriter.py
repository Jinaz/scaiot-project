from IOTHubSensors import Datagatherer as dg
import DataFiles.Constants as ss
def write_problem(filename= ss.TEST_PROBLEM,wanted_temp=24,wanted_lightlevel=30,
                  outside_temp = 30,heaterstatus=False,coolerstatus=False,
                  windowstatus=False,doorstatus=False,curtainstatus=False,
                  presentation=False,inlecture=True,betweenLectures=False,
                  afterLecture=False,firstLecture=False,weather=0):
    humidity, temperature, lightlevel, ir_value = dg.readData()
    f = open(filename, "w")
    f.write(ss.PDDLCONTENT)

    f.close()