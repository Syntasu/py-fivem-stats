from snaphot import Snapshotter
from api import ServerListApi
from saver import Saver

def main():
    serverListApi = ServerListApi()
    json = serverListApi.Fetch()

    snapshotter = Snapshotter(json)
    snapshot = snapshotter.MakeSnapshot()

    fileSaver = Saver()
    fileSaver.Save(snapshot)

    print(snapshot)

if __name__ == "__main__":
    main()
