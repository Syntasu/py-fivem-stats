from snaphot import Snapshotter
from api import ServerListApi

def main():
    serverListApi = ServerListApi()
    json = serverListApi.Fetch()

    snapshotter = Snapshotter(json)
    snapshot = snapshotter.MakeSnapshot()

    print(snapshot)

if __name__ == "__main__":
    main()
