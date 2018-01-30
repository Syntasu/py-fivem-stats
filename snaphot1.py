import json
import time

class Snapshotter:
    def __init__(self, data):
        self.data = data
        self.output = {}
    
    def MakeSnapshot(self): 
        self.output["date"] = time.strftime("%x")
        

        return json.dumps(self.output)
    