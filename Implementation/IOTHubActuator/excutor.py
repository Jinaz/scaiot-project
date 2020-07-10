def dimlightsUp():
    print("manager informed")
    pass


def heater_On():
    print("manager informed")
    pass


def heater_Off():
    print("manager informed")
    pass


def cooler_On():
    print("manager informed")
    pass


def cooler_Off():
    print("manager informed")
    pass


def open_Windows():
    import DoorWindowControl.WindowControl as wc
    wc.openWindow()
    print("manager informed")
    pass


def close_Windows():
    import DoorWindowControl.WindowControl as wc
    wc.closeWindow()
    print("manager informed")
    pass


def nothing():
    print("manager informed")
    pass


def refresh_air():
    print("manager informed")
    import DoorWindowControl.WindowControl as wc
    wc.openWindow()
    pass


def dimLightsup():
    print("manager informed")
    import LightControl.L_Control as lc
    lc.signal("mid")
    pass


def dimLightsdown():
    print("manager informed")
    import LightControl.L_Control as lc
    lc.signal("mid")
    pass


def fullLights():
    print("manager informed")
    import LightControl.L_Control as lc
    lc.signal("on")
    pass


def lightsOff():
    print("manager informed")
    import LightControl.L_Control as lc
    lc.signal("off")
    pass


def curtain_up():
    print("manager informed")
    pass


def curtain_down():
    print("manager informed")
    pass


def unlockRoom():
    import DoorWindowControl.doorControl as dc
    dc.openDoor()
    print("manager informed")
    pass


def lockRoom():
    import DoorWindowControl.doorControl as dc
    dc.closeDoor()
    print("manager informed")
    pass
