import PddlFiles.pddlLoop as pl
import IOTHubActuator.decider as decider
import IOTHubSensors.SensorLoop as gathering
import time
import DATA.dummyGenerator as dg
if __name__ == "__main__":
    #dg.generateDummy()
    system = "calculating"#"gathering" #"calculating"
    if system == "gathering":
        gathering.main_On_Py()
    elif system == "calculating":
        while True:
            actions = pl.pddlLoop()

            decider.decide(actions)

            time.sleep(10)


