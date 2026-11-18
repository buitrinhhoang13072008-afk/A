import random
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
    def drive(self,hours):
        self.distance += hours*self.speed

    def show(self):
        print(f"the car's registration number is {self.reg}")
        print(f"the car's max speed is {self.maxs}")
        print(f"the car's distance is {self.distance}")
        print("\n")
cars = []
for i in range(1, 11):
    maxs = random.randint(100, 200)
    reg = f"ABC-{i}"
    cars.append(car(reg, maxs))
while max(c.distance for c in cars) < 10000:
    for c in cars:
        acceleration = random.randint(-10, 15)
        c.accelerate(acceleration)
        c.drive(1)
for c in cars:
    c.show()