class Person(object):
    species = "Homo Species"
    def __init__(self, *args):
        self.args = args
        for val in args:
            print(val)
        print(self.args)
Person("AA", "BB")

