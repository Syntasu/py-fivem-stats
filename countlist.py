import json

class CountList:
    
    def __init__(self):
        self.buffer = {}

    def Occurrence(self, key):
        if key in self.buffer:
            self.buffer[key] = self.buffer[key] + 1
        else:
            self.buffer[key] = 1

    def GetResult(self):
        return self.buffer