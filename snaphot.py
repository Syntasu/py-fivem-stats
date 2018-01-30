import re
import json
import time
from cache import Cache

class Snapshotter:
    def __init__(self, data):
        self.data = data
        self.output = {}
        self.cache = Cache()

    def MakeSnapshot(self):
        self.output["date"] = time.strftime("%x")

        for index, serverData in enumerate(self.data):
            currentServerData = serverData["Data"]
            self.processServerData(currentServerData)

            if "vars" in currentServerData:
                self.processVarsData(currentServerData["vars"])

        self.generateOutput()

        return json.dumps(self.output, sort_keys=True, indent=4)

    def processServerData(self, serverData):
        serverClients = serverData["clients"]
        serverMaxClients = serverData["sv_maxclients"]

        if serverClients == 0:
            self.cache.Increment("server_empty", 1)

        elif serverClients >= serverMaxClients:
            self.cache.Increment("server_full", 1)
        
        serverVersion = serverData["server"]
        match = re.search('FXServer-master SERVER v1.0.0.(.+?) win32', serverVersion)

        if match:
            print(match.group(1))

        self.cache.Increment("max_client_count", serverMaxClients)
        self.cache.Increment("client_count", serverData["clients"])
        self.cache.Increment("server_count", 1)

    def processVarsData(self, varData):
        scriptHookVar = varData["sv_scriptHookAllowed"]
        if json.loads(scriptHookVar):
            self.cache.Increment("scripthook_enabled", 1)
        else:
            self.cache.Increment("scripthook_disabled", 1)

    def generateOutput(self):
        self.output["svCount"] = self.cache.Get("server_count")                                             # Servers count
        self.output["svFull"] = self.cache.Get("server_full")                                               # Servers that are full
        self.output["svEmpty"] = self.cache.Get("server_empty")                                             # Servers that are empty
        self.output["svAvgSlots"] = self.cache.Get("max_client_count") / self.cache.Get("server_count")     # Server average slot count.
        
        self.output["svVarScriptHookEnabled"] = self.cache.Get("scripthook_enabled")                        # Count of server with scripthook enabled
        self.output["svVarScriptHookDisabled"] = self.cache.Get("scripthook_disabled")                      # Count of server with scripthook disabled
        
        self.output["clCount"] = self.cache.Get("client_count")                                             # Total client count.
        self.output["ptsRatio"] = (self.cache.Get("client_count") / self.cache.Get("server_count"))         # Ratio of player per server.
