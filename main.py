import asyncio
import time
import random
 
from snaphot import Snapshotter
from api import ServerListApi
from saver import Saver
from timed import TimedTask

serverListApi = ServerListApi()
fileSaver = Saver()

def TakeSnapshot():
    json = serverListApi.Fetch()
    snapshotter = Snapshotter(json)
    snapshot = snapshotter.MakeSnapshot()
    fileSaver.Save(snapshot)

def SquashHourly():
    print("Squash me senpai")

def SquashDaily():
    print("Squash me senpai")

def SquashMonthly():
    print("Squash me senpai")

def Say():
    print("Hello world!")

fetchServerListTask = TimedTask(10 * 60, TakeSnapshot)
squashSnapshotsHourly = TimedTask(60 * 60, SquashHourly)
squashSnapshotsDaily = TimedTask(24 * 60 * 60, SquashDaily)
squashSnapshotsMonthly = TimedTask(30 * 24 * 60 * 60, SquashMonthly)


while True:
    fetchServerListTask.Poll()
    squashSnapshotsHourly.Poll()
    squashSnapshotsDaily.Poll()
    squashSnapshotsMonthly.Poll()


