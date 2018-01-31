import json
import operator
from collections import OrderedDict
from collections import Counter
import heapq


class CountList:
    
    def __init__(self):
        self.buffer = OrderedDict()

    def Occurrence(self, key):
        if key in self.buffer:
            self.buffer[key] = self.buffer[key] + 1
        else:
            self.buffer[key] = 1

    def GetResult(self):
        return self.buffer

    def GetResultTop(self, count):

        top = dict(sorted(self.buffer.items(), reverse=True, key=lambda x: x[1])[:count])
        return top