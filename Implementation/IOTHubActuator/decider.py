from IOTHubActuator import excutor as ex


def decide(actions,room):
    for action in actions:
        if action == 'heater_On':
            ex.heater_On()
            room.heater.status = 1
        if action == 'heater_Off':
            ex.heater_Off()
        if action == 'cooler_On':
            ex.cooler_On()
        if action == 'cooler_Off':
            ex.cooler_Off()
        if action == 'open_Windows':
            ex.open_Windows()
        if action ==  'close_Windows':
            ex.close_Windows()
        if action ==  'nothing':
            ex.nothing()
        if action ==  'refresh_air':
            ex.refresh_air()
        if action == 'dimLightsup':
            ex.dimlightsUp()
        if action ==  'dimLightsdown':
            ex.dimLightsdown()
        if action ==  'fullLights':
            ex.fullLights()
        if action ==  'lightsOff':
            ex.lightsOff()
        if action == 'curtain_up':
            ex.curtain_up()
        if action ==  'curtain_down':
            ex.curtain_down()
            room.curtain.status = 1
        if action ==  'unlockRoom':
            ex.unlockRoom()
        if action ==  'lockRoom':
            ex.lockRoom()