from pathlib import Path

import Actuators.WindowControl as wc
import Actuators.L_Control as lc
import Actuators.doorControl as dc
import sys

import RoomModel

ROOMJSON = "../Implementation/DATA/room.json"
TRIGGERFILE = "../Implementation/DATA/trigger.llz"

def loadRoom():
    room = RoomModel.initRoom()
    roomfile = Path(ROOMJSON)
    if roomfile.is_file():
        # file exists
        import json

        with open(ROOMJSON) as json_file:
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

    return room

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "roomstatus":
            room = loadRoom()
            print("room name:",room.name)
            print("window name:", room.window.name, "window status", "open"if room.window.status == 1 else "closed")
            print("curtain name:", room.curtain.name, "curtain status", "down" if room.curtain.status == 1 else "up")
            print("heater name:", room.heater.name, "heater status", "on" if room.heater.status == 1 else "off")
            print("air conditioner name:", room.cooler.name, "air conditioner status", "on" if room.cooler.status == 1 else "off")
            lightstatus = "off"
            if room.light.status == 1:
                lightstatus = "dimmed"
            elif room.light.status == 2:
                lightstatus = "on"
            print("light name:", room.light.name, "light status", lightstatus)

        if command == "heater_on":
            room = loadRoom()
            if room.heater.status == 1:
                print("heater already on")
            else:
                room.heater.status = 1
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()

        if command == "heater_off":
            room = loadRoom()
            if room.heater.status == 0:
                print("heater already off")
            else:
                room.heater.status = 1
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()

        if command == "cooler_on":
            room = loadRoom()
            if room.cooler.status == 1:
                print("air conditioner already on")
            else:
                room.cooler.status = 1
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()

        if command == "cooler_off":
            room = loadRoom()
            if room.cooler.status == 0:
                print("air conditioner already off")
            else:
                room.cooler.status = 0
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()

        if command == "window_open":
            room = loadRoom()
            if room.window.status == 1:
                print("windows already open")
            else:
                wc.openWindow()
                room.window.status = 1
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()

        if command == "window_close":
            room = loadRoom()
            if room.window.status == 0:
                print("windows already closed")
            else:
                wc.closeWindow()
                room.window.status = 0
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()
        if command == "light_off":
            room = loadRoom()
            if room.light.status == 0:
                print("lights already off")
            else:
                lc.signal("off")
                room.light.status = 0
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()
        if command == "light_dim":
            room = loadRoom()
            if room.light.status == 1:
                print("lights already dimmed")
            else:
                lc.signal("mid")
                room.light.status = 1
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()
        if command == "light_on":
            room = loadRoom()
            if room.light.status == 2:
                print("lights already on")
            else:
                lc.signal("on")
                room.light.status = 2
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()
        if command == "lock_door":
            room = loadRoom()
            if room.door.status == 1:
                print("door already locked")
            else:
                dc.closeDoor()
                room.door.status = 1
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()
        if command == "unlock_door":
            room = loadRoom()
            if room.door.status == 0:
                print("door already unlocked")
            else:
                dc.openDoor()
                room.door.status = 0
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()
        if command == "curtain_up":
            room = loadRoom()
            if room.curtain.status == 0:
                print("curtain already up")
            else:
                room.curtain.status = 0
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()
        if command == "curtain_down":
            room = loadRoom()
            if room.curtain.status == 1:
                print("curtain already down")
            else:
                room.curtain.status = 1
                room.saveConfig()
                f = open(TRIGGERFILE, "w")
                f.write("True")
                f.close()
    else:
        print("invalid command")

