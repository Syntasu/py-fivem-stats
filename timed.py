from datetime import datetime


class TimedTask():
    def __init__(self, interval, func):
        self.interval = interval
        self.func = func
        self.last = datetime.now()

    def Poll(self):
        start = datetime.now()
        delta = start - self.last

        if(delta.total_seconds() >= self.interval):
            self.func()
            self.last = datetime.now()

