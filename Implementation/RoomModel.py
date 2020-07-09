class Room():
    def __init__(self, name, window, light, heater, cooler, curtain, door,presenting=False):
        self.name = name
        self.window = window
        self.light = light
        self.heater = heater
        self.cooler = cooler
        self.curtain = curtain
        self.door = door
        self.presenting = presenting

    def getName(self):
        return self.name

    def getWindow(self):
        return self.window

    def getLights(self):
        return self.light

    def getHeater(self):
        return self.heater

    def getCooler(self):
        return self.cooler

    def getCurtain(self):
        return self.curtain

    def getDoor(self):
        return self.door


class Window():
    def __init__(self, name, status=0):
        self.name = name
        self.status = status

    def getStatus(self):
        return self.status

    def getName(self):
        return self.name


class Light():
    def __init__(self, name, status=0):
        self.name = name
        self.status = status

    def getStatus(self):
        return self.status

    def getName(self):
        return self.name


class Heater():
    def __init__(self, name, status=0):
        self.name = name
        self.status = status

    def getStatus(self):
        return self.status

    def getName(self):
        return self.name


class Cooler():
    def __init__(self, name, status=0):
        self.name = name
        self.status = status

    def getStatus(self):
        return self.status

    def getName(self):
        return self.name


class Curtain():
    def __init__(self, name, status=0):
        self.name = name
        self.status = status

    def getStatus(self):
        return self.status

    def getName(self):
        return self.name


class Door():
    def __init__(self, name, status=0):
        self.name = name
        self.status = status

    def getStatus(self):
        return self.status

    def getName(self):
        return self.name


def initRoom(roomname="r0", windowname="w0", lightname="l0", heatername="h0", coolername="c0", curtainname="c0",
             doorname="d0"):
    door = Door(doorname)
    window = Window(windowname)
    light = Light(lightname)
    heater = Heater(heatername)
    cooler = Cooler(coolername)
    curtain = Curtain(curtainname)
    room = Room(roomname, window, light, heater, cooler, curtain, door)

    return room
