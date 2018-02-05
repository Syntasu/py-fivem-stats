import asyncio
import time
import random
 
from snaphot import Snapshotter
from api import ServerListApi
from saver import Saver

serverListApi = ServerListApi()
fileSaver = Saver()

def TakeSnapshot():
    json = serverListApi.Fetch()
    snapshotter = Snapshotter(json)
    snapshot = snapshotter.MakeSnapshot()
    fileSaver.Save(snapshot)

TakeSnapshot()

from datetime import datetime, date

delay = 15 * 60
end = datetime.now()
while True:
    start = datetime.now()
    delta = start - end

    if(delta.total_seconds() > delay):
        print("MADE SNAPHOT")
        end = datetime.now()

