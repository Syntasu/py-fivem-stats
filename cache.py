class Cache:

    internalCache = {}

    def __create(self, key, default):
        if not key in self.internalCache:
            self.internalCache[key] = default

    def Get(self, key):
        self.__create(key, 0)
        return self.internalCache[key]

    def Set(self, key, value):
        self.__create(key, 0)
        self.internalCache[key] = value

    #only works for integers.
    def Increment(self, key, amount):
        original = self.Get(key)

        if type(original) == int:
            self.Set(key, original + amount)  