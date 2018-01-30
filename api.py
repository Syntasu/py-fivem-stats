from urllib.request import Request, urlopen

class ServerListApi:

    ServerURL = "http://servers-live.fivem.net/api/servers/"

    def Fetch(self):
        request = Request(self.ServerURL)
        request.add_header('User-Agent', "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46")

        response = urlopen(request).read()

        print(response);