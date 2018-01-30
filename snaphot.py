import json
import time
import dictHelper

class Snapshotter:
    def __init__(self, data):
        self.data = data
        self.output = {}
        self.cache = {}

    def MakeSnapshot(self):
        self.output["date"] = time.strftime("%x")

        for index, serverData in enumerate(self.data):
            self.processServerData(serverData["Data"])

        self.finalizeServerData()

        return json.dumps(self.output, sort_keys=True, indent=4)

    def processServerData(self, serverData):
        dictHelper.increment(self.cache, "client_sum", serverData["clients"])
        dictHelper.increment(self.cache, "server_count", 1)

    def finalizeServerData(self):
        self.output["playerToServerRatio"] = (self.cache["client_sum"] / self.cache["server_count"])
