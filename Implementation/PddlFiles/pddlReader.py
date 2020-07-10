import DataFiles.Constants as names

def readAction(response):
    actions = []
    for resp in response:
        for action in names.ACTIONS:
            if resp.find(action.lower()) != -1:
                actions.append(action)

    print("actions to take:",actions)
    return actions