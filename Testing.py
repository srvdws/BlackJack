class Test():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return('my name is {}'.format(self.name))

manetest = Test('kylr')

print(manetest)