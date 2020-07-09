import PddlFiles.pddlLoop as pl
import IOTHubActuator.decider as decider
import IOTHubSensors.SensorLoop as gathering
import time
import sys
import DATA.dummyGenerator as dg
if __name__ == "__main__":
    #dg.generateDummy()
    system = "gathering"
    #print(sys.argv)
    if len(sys.argv) == 2 and sys.argv[1] == "calc":
        system = "calculating"
    #system = "calculating"#"gathering" #"calculating"
    if system == "gathering":
        gathering.main_On_Py()
    elif system == "calculating":
        while True:
            actions = pl.pddlLoop()

            decider.decide(actions)

            time.sleep(10)


