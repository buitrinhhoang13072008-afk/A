class car:
    def __init__(self,reg, maxs):
        self.reg = reg
        self.maxs = maxs
        self.speed =0
        self.distance = 0
    def show(self):
        print(f"the car's registration number is {self.reg}")
        print(f"the car's max speed is {self.maxs}")
a = car("ADB-1234", 123)
b = car("asdas",1234)
a.show()
b.show()