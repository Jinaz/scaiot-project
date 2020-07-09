import time
import DataFiles.Constants as CTS

def triggerDataStore():
    file = open(CTS.TRIGGERPATH, "w")
    file.write("True")
    file.close()

    time.sleep(1)
    file = open(CTS.TRIGGERPATH, "w")
    file.write("False")
    file.close()

    print("data recorded")

triggerDataStore()