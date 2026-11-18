class car:
    def __init__(self,reg, maxs):
        self.reg = reg
        self.maxs = maxs
        self.speed =0
        self.distance = 0
    def accelerate(self, acceleration):
        if self.speed +acceleration > self.maxs:
            self.speed = self.maxs
        elif self.speed + acceleration < 0:
            self.speed =0
        else:
            self.speed += acceleration
    def show(self):
        print(f"the car's registration number is {self.reg}")
        print(f"the car's max speed is {self.maxs}")
a = car("ADB-1234", 123)
b = car("asdas",1234)
a.accelerate(10)
print (a.speed)