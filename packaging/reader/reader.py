class Reader(object):
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, 'r')

    def close(self):
        self.f.close()

    def read(self):
        print(self.f.read())
