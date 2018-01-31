import time

class Saver:

    def Save(self, data):
        try:
            snapShotname = "Snapshot_" + time.strftime("%d-%m-%y_%H-%M-%S") + ".json"
            snapshot = open(snapShotname, "w")
            snapshot.write(data)
            snapshot.close()
        except IOError:
            print("could not write log files")
