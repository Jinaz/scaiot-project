from IOTHubSensors import Datagatherer as dg
import DataFiles.Constants as ss


def write_problem(room, filename=ss.TEST_PROBLEM, wanted_temp=24, wanted_lightlevel=30,
                  outside_temp=30, heaterstatus=0, coolerstatus=0, lightstatus=0,
                  windowstatus=0, doorstatus=0, curtainstatus=0,
                  presentation=False, inlecture=True, betweenLectures=False,
                  afterLecture=False, firstLecture=False, roomIsEmpty=False, weather=0):
    humidity, temperature, lightlevel, ir_value = dg.readData()

    roomname = room.name
    windowname = room.window.name
    coolername = room.cooler.name
    heatername = room.heater.name
    doorname = room.door.name
    lightname = room.light.name
    curtainname = room.curtain.name

    template = ss.PDDLTemplate
    we = "(isSunny outside)"
    if weather == 1:
        we = "(isCloudy outside)"
    elif weather == 2:
        we = "(isRainy outside)"
    elif weather == 3:
        we = "(isSnowing outside)"

    re = "(not(roomEmpty {}))".format(roomname)
    if roomIsEmpty:
        re = "(roomEmpty {})".format(roomname)

    ct = "(inLectureTime {})".format(roomname)
    if betweenLectures:
        ct = "(betweenLectures {})".format(roomname)
    elif afterLecture:
        ct = "(lectureTimeOver {})".format(roomname)
    elif firstLecture:
        ct = "(firstlecture {})".format(roomname)

    prop1 = "(has_window {} {})".format(roomname, windowname)
    prop2 = "(has_door {} {})".format(roomname, doorname)
    prop3 = "(has_cooler {} {})".format(coolername, roomname)
    prop4 = "(has_heater {} {})".format(heatername, roomname)
    prop5 = "(has_light {} {})".format(roomname, lightname)
    prop6 = "(has_curtain {} {})".format(roomname, curtainname)
    prop7 = "(not (output-done {}))".format(roomname)

    present = "(presentingInRoom {})".format(roomname)
    if not presentation:
        present = "(notpresentingInRoom {})".format(roomname)

    custat = "(are_up {})".format(curtainname)
    if curtainstatus == 1:
        custat = "(are_up {})".format(curtainname)

    lightstat = "(are_off {})".format(lightname)
    if lightstatus == 1:
        lightstat = "(are_dimmed {})".format(lightname)
    elif lightstatus == 2:
        lightstat = "(are_fully_on {})".format(lightname)

    winstat = "(are_closed {})".format(windowname)
    if windowstatus == 1:
        winstat = "(are_open {})".format(windowname)

    doorstat = "(is_unlocked {})".format(doorname)
    if doorstatus == 1:
        doorstat = "(is_locked {})".format(doorname)

    heatstat = "(is_off_heat {})".format(heatername)
    if heaterstatus == 1:
        heatstat = "(is_on_heat {})".format(heatername)

    coolstat = "(is_off_cool {})".format(coolername)
    if coolerstatus == 1:
        coolstat = "(is_off_cool {})".format(coolername)

    wantedTemp = "(= (temperature_wanted {}) {})".format(roomname, wanted_temp)
    actTemp = "(= (actual_temp {}) {})".format(roomname, temperature)
    outtemp = "(= (outside_temp) {})".format(outside_temp)
    # debug Variable
    outputVar = "(= (outtemp) {})".format(0)

    insidelightlevel = "(=(actual_lightlevel {}) {})".format(roomname, lightlevel)
    wantedLL = "(=(wantedLightlevel {}) {})".format(roomname, wanted_lightlevel)
    wantedLLPPT = ""
    if wanted_lightlevel - 10 > 0:
        wantedLLPPT = "(=(wantedLightlevelPPT {}) {})".format(roomname, wanted_lightlevel - 10)
    else:
        wantedLLPPT = "(=(wantedLightlevelPPT {}) {})".format(roomname, wanted_lightlevel)

    goal = "(output-done {})".format(roomname)

    content = template.format(roomname, windowname, coolername, heatername, doorname, lightname, curtainname,
                    we, re, ct, prop1, prop2, prop3, prop4, prop5, prop6, prop7, present, custat, lightstat, winstat,
                    doorstat, heatstat, coolstat, wantedTemp, actTemp, outtemp, outputVar, insidelightlevel,
                    wantedLL, wantedLLPPT, goal)

    f = open(filename, "w")
    f.write(content)

    f.close()
