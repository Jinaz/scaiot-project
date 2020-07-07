import requests, sys

data = {'domain': open('domain.pddl', 'r').read(),
        'problem': open('problem.pddl', 'r').read()}

resp = requests.post('http://solver.planning.domains/solve',
                     verify=False, json=data).json()

with open('plan.plan', 'w') as f:
    f.write('\n'.join([act['name'] for act in resp['result']['plan']]))
