import requests
import DataFiles.Constants as names
from PddlFiles import pddlReader as reader, pddlWriter as writer

import time


def getPlan():
    data = {'domain': open(names.DOMAIN, 'r').read(),
            'problem': open(names.TEST_PROBLEM, 'r').read()}

    resp = requests.post('http://solver.planning.domains/solve',
                         verify=False, json=data).json()
    #print(resp)
    try:
        with open(names.OUTPUTFILE, 'w') as f:
            f.write('\n'.join([act['name'] for act in resp['result']['plan']]))

        response = [act['name'] for act in resp['result']['plan']]
        # print(response)

        return response
    except:
        print("no plan found")
        return []


def pddlLoop():

    resp = getPlan()

    #time.sleep(2)
    actions = reader.readAction(resp)

    return actions
