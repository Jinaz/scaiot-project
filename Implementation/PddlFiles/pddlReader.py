import DataFiles.Constants as names

def readAction(response):
    #f = open(names.OUTPUTFILE, "r")
    #decision = f.readlines()
    actions = []
    for resp in response:
        #for line in decision:
        for action in names.ACTIONS:
            if resp.find(action.lower()) != -1:
                actions.append(action)

    print("actions to take:",actions)
    return actions