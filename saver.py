import time
import os

class Saver:

    def Save(self, data):

        folder = "snapshots/"

        self.__checkDir(folder)
        
        try:
            snapShotname = "Snapshot_" + time.strftime("%d-%m-%y_%H-%M-%S") + ".json"
            snapshot = open(folder + snapShotname, "w")
            snapshot.write(data)
            snapshot.close()
        except IOError:
            print("could not write log files")


    def __checkDir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
