import PddlFiles.pddlLoop as pl
import IOTHubActuator.decider as decider
import IOTHubSensors.SensorLoop as gathering
import time
import sys
import DataFiles.Constants as con
import DATA.dummyGenerator as dg
import RoomModel
import PddlFiles.pddlWriter as writer

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

        while True:
            # TODO get time and weather
            weather = 0

            # TODO set the flags depending on current time and calendar
            crtime = 0
            inlecture = True
            betweenLectures = False
            afterLecture = False
            firstLecture = False
            roomIsEmpty = False
            #print(room.presenting)

            writer.write_problem(room, con.TEST_PROBLEM, 30, 30, 30, room.heater.status, room.cooler.status,
                                 room.light.status,
                                 room.window.status, room.door.status, room.curtain.status, room.presenting,
                                 inlecture, betweenLectures, afterLecture, firstLecture, roomIsEmpty, 0)
            time.sleep(2)

            actions = pl.pddlLoop()

            decider.decide(actions, room)

            time.sleep(10)
