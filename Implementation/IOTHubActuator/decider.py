from IOTHubActuator import excutor as ex


def generate_content(actions, room):
    content = "based on the current situation, following plan was made:\n"
    count = 0
    for action in actions:
        count += 1
        if action == 'heater_On':
            content += str(count) + ". " + "please turn on heater\n"
            ex.heater_On()
            room.heater.status = 1
        if action == 'heater_Off':
            content += str(count) + ". " + "please turn off heater\n"
            ex.heater_Off()
        if action == 'cooler_On':
            content += str(count) + ". " + "please turn on air condition\n"
            ex.cooler_On()
        if action == 'cooler_Off':
            content += str(count) + ". " + "please turn off air condition\n"
            ex.cooler_Off()
        if action == 'open_Windows':
            content += str(count) + ". " + "please open the windows\n"
            ex.open_Windows()
        if action ==  'close_Windows':
            content += str(count) + ". " + "please close the windows\n"
            ex.close_Windows()
        if action ==  'nothing':
            ex.nothing()
        if action ==  'refresh_air':
            content += str(count) + ". " + "please open the windows between lectures (recommended)\n"
            ex.refresh_air()
        if action == 'dimLightsup':
            content += str(count) + ". " + "please turn up the lights a little\n"
            ex.dimlightsUp()
        if action ==  'dimLightsdown':
            content += str(count) + ". " + "please dim the lights\n"
            ex.dimLightsdown()
        if action ==  'fullLights':
            content += str(count) + ". " + "please turn on the lights\n"
            ex.fullLights()
        if action ==  'lightsOff':
            content += str(count) + ". " + "please turn off the lights\n"
            ex.lightsOff()
        if action == 'curtain_up':
            content += str(count) + ". " + "please open the curtain\n"
            ex.curtain_up()
        if action ==  'curtain_down':
            content += str(count) + ". " + "please close the curtain\n"
            ex.curtain_down()
            room.curtain.status = 1
        if action ==  'unlockRoom':
            content += str(count) + ". " + "please open the lecture room\n"
            ex.unlockRoom()
        if action ==  'lockRoom':
            content += str(count) + ". " + "please close the lecture room\n"
            ex.lockRoom()

    return content