class DB_item:
    def __init__(self):
        self.DB = {}
        self.DB_Past = {}

    def Create(self, key):
        self.key = key
        self.DB[self.key] = []

    def add(self, value, key = None):
        if key == None:
            key = self.key
        self.DB[key] = self.DB[key] + value

    def print(self, key=None):
        if key == None:
            key = self.key
        print(self.DB[key])

    def keys(self):
        print(list(self.DB.keys()))

    def pop(self, key = None):
        self.initkey(key)


    def initkey(self, key):
        if key == None:
            key = self.key

if __name__ == '__main__':
    a = DB_item()
    a.Create("size")

    a.add([200, 100, 300, 400])
    a.print()
    a.keys()
