class Fan():
    def describe(self):
        print("General fan")
class Computer(Fan):
    def describe(self):
        print("Computer's internal fan")
class House(Fan):
    def describe(self):
        print("House fan")
f=Fan()
c=Computer()
h=House()
f.describe()
c.describe()
h.describe()