import sys
import codecs
import re
import json
import time
from cache import Cache
from countlist import CountList

class Snapshotter:
    def __init__(self, data):
        self.data = data
        self.output = []
        self.cache = Cache()
        self.versionCount = CountList()
        self.resourceCount = CountList()

    def MakeSnapshot(self):
        for index, serverData in enumerate(self.data):
            currentServerData = serverData["Data"]
            self.processServerData(currentServerData)

            if "vars" in currentServerData:
                self.processVarsData(currentServerData["vars"])

            if "resources" in currentServerData:
                self.processResources(currentServerData["resources"])

        self.generateOutput()

        return json.dumps(self.output)

    def processServerData(self, serverData):
        serverClients = serverData["clients"]
        serverMaxClients = serverData["sv_maxclients"]

        if serverClients == 0:
            self.cache.Increment("server_empty", 1)

        elif serverClients >= serverMaxClients:
            self.cache.Increment("server_full", 1)

        if serverMaxClients > self.cache.Get("server_max_slots"):
            self.cache.Set("server_max_slots", serverMaxClients)

        if serverMaxClients < self.cache.Get("server_min_slots") or self.cache.Get("server_min_slots") == 0:
            self.cache.Set("server_min_slots", serverMaxClients)
        
        match = re.search('FXServer-master SERVER v1.0.0.(.+?) win32', serverData["server"])

        if match:
            self.versionCount.Occurrence(match.group(1))

        self.cache.Increment("max_client_count", serverMaxClients)
        self.cache.Increment("client_count", serverData["clients"])
        self.cache.Increment("server_count", 1)

    def processVarsData(self, varData):
        scriptHookVar = varData["sv_scriptHookAllowed"]
        if json.loads(scriptHookVar):
            self.cache.Increment("scripthook_enabled", 1)
        else:
            self.cache.Increment("scripthook_disabled", 1)

    def processResources(self, resourceData):
        for item in resourceData:
            self.resourceCount.Occurrence(item)

    def generateOutput(self):
        self.output.append(time.strftime("%d-%m-%y_%H:%M:%S"))                                      # Snapshot date
        self.output.append(self.cache.Get("server_count"))                                          # Servers count
        self.output.append(self.cache.Get("server_full"))                                           # Servers that are full
        self.output.append(self.cache.Get("server_empty"))                                          # Servers that are empty
        self.output.append(self.cache.Get("max_client_count") / self.cache.Get("server_count"))     # Server average slot count.
        self.output.append(self.cache.Get("server_max_slots"))                                      # Server with highest slot count.
        self.output.append(self.cache.Get("server_min_slots"))                                      # Server with lowest slot count.
        self.output.append(self.versionCount.GetResult())                                           # Count of all server versions.
        self.output.append(self.resourceCount.GetResultTop(50))                                     # Count all the resources of the server
        self.output.append(self.cache.Get("scripthook_enabled"))                                    # Count of server with scripthook enabled
        self.output.append(self.cache.Get("scripthook_disabled"))                                   # Count of server with scripthook disabled
        self.output.append(self.cache.Get("client_count"))                                          # Total client count.
