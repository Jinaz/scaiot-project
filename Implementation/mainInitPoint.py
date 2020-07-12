import PddlFiles.pddlLoop as pl
import IOTHubActuator.decider as decider
import time
import sys
import DataFiles.Constants as con
import DATA.dummyGenerator as dg
import WeatherForecast.weatherReaderPy as wrp
import SmartCitiesCalendar.calendarreader as crp
import RoomModel
import PddlFiles.pddlWriter as writer
from pathlib import Path
import InformActuator.sendEmail as se
from IOTHubSensors import SensorHub as sh
import numpy as np
import datetime

def loadRoom():
    room = RoomModel.initRoom()
    roomfile = Path(con.ROOMJSON)
    if roomfile.is_file():
        # file exists
        import json

        with open(con.ROOMJSON) as json_file:
            data = json.load(json_file)
            room.curtain.name = data["curtain"]["name"]
            room.curtain.status = data["curtain"]["status"]

            room.heater.name = data["heater"]["name"]
            room.heater.status = data["heater"]["status"]

            room.light.name = data["light"]["name"]
            room.light.status = data["light"]["status"]

            room.door.name = data["door"]["name"]
            room.door.status = data["door"]["status"]

            room.cooler.name = data["cooler"]["name"]
            room.cooler.status = data["cooler"]["status"]

            room.window.name = data["window"]["name"]
            room.window.status = data["window"]["status"]
            print("data loaded")

    import LightControl.L_Control as lc
    lc.initial()
    room.light.status = 0
    import DoorWindowControl.WindowControl as wc
    wc.closeWindow()
    room.window.status = 0
    import DoorWindowControl.doorControl as dc
    dc.closeDoor()
    room.door.status = 1

    return room

if __name__ == "__main__":
    room = loadRoom()
    loopcount = 0
    datacontainer = np.zeros((4, 10))
    current_time = datetime.datetime.fromisoformat('2020-07-13 08:05:00+02:00')
    while True:
        #hook to manipulate status from outside
        f = open(con.TRIGGERPATH)
        c = f.read(4)
        if c == "True":
            room = loadRoom()
            f2 = open(con.TRIGGERPATH, "w")
            f2.write("False")
            f2.close()

        # inLecture = True
        # betweenLectures = False
        # afterLastLecture = False
        # shortBeforeFirstLecture = False

        # print(room.presenting)
        inLecture, betweenLectures, afterLastLecture, shortBeforeFirstLecture = crp.readurl(current_time)
        outtemp, weather = wrp.readurl()

        humidity, temperature, lightlevel, ir_value = sh.getData()
        # humidity, temperature, lightlevel, ir_value = daga.readData()
        datacontainer[0][loopcount] = humidity
        datacontainer[1][loopcount] = temperature
        datacontainer[2][loopcount] = lightlevel
        datacontainer[3][loopcount] = ir_value


        #def write_problem(room, filename=ss.TEST_PROBLEM, wanted_temp=24, wanted_lightlevel=400,
                          #outside_temp=30, heaterstatus=0, coolerstatus=0, lightstatus=0,
                          #windowstatus=0, doorstatus=0, curtainstatus=0,
                          #presentation=False, inlecture=True, betweenLectures=False,
                          #afterLecture=False, firstLecture=False, weather=0, tem=-1, hum=-1, lightl=-1, ir_val=-1):
        writer.write_problem(room, con.TEST_PROBLEM, con.DESIRED_TEMP, con.DESIRED_LIGHTLEVEL, outtemp,
                             room.heater.status, room.cooler.status,
                             room.light.status,
                             room.window.status, room.door.status, room.curtain.status, room.presenting,
                             inLecture, betweenLectures, afterLastLecture, shortBeforeFirstLecture, weather, temperature, humidity,
                             lightlevel, ir_value)
        # time.sleep(2)

        actions = pl.pddlLoop()
        if len(actions) > 0:
            emailcontent = decider.generate_content(actions, room)
            se.sendEmail("noreply.scaiot.project@gmail.com", emailcontent)
            room.saveConfig()
        time.sleep(1)
        current_time += datetime.timedelta(minutes=10, seconds=0)

        loopcount += 1
        if loopcount % 10 == 0:
            from numpy import savetxt

            loopcount = 0
            data0 = datacontainer[0, :]
            data1 = datacontainer[1, :]
            data2 = datacontainer[2, :]
            data3 = datacontainer[3, :]
            # save to csv file
            savetxt('DATA/hum.csv', data0, delimiter=',')
            savetxt('DATA/temp.csv', data1, delimiter=',')
            savetxt('DATA/light.csv', data2, delimiter=',')
            savetxt('DATA/ir_data.csv', data3, delimiter=',')
