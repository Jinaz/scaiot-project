import PddlFiles.pddlLoop as pl
import IOTHubActuator.decider as decider
import IOTHubSensors.SensorLoop as gathering
import time
import sys
import DataFiles.Constants as con
import DATA.dummyGenerator as dg
import WeatherForecast.weatherReaderPy as wrp
import RoomModel
import PddlFiles.pddlWriter as writer
from pathlib import Path

if __name__ == "__main__":

    system = "gathering"
    # print(sys.argv)
    if len(sys.argv) == 2 and sys.argv[1] == "calc":
        system = "calculating"
    # system = "calculating"#"gathering" #"calculating"
    if system == "gathering":
        gathering.main_On_Py()
    elif system == "calculating":

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


        while True:

            # TODO set the flags depending on current time and calendar
            crtime = 0
            inlecture = True
            betweenLectures = False
            afterLecture = False
            firstLecture = False

            #print(room.presenting)
            outtemp ,weather = wrp.readurl()

            writer.write_problem(room, con.TEST_PROBLEM, 30, 30, outtemp, room.heater.status, room.cooler.status,
                                 room.light.status,
                                 room.window.status, room.door.status, room.curtain.status, room.presenting,
                                 inlecture, betweenLectures, afterLecture, firstLecture, weather)
            time.sleep(2)

            actions = pl.pddlLoop()

            decider.decide(actions, room)

            time.sleep(10)
