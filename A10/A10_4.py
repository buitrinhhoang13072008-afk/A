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
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for c in self.cars:
            acceleration = random.randint(-10, 15)
            c.accelerate(acceleration)
            c.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("-" * 75)
        print(f"{'Registration':<15}{'Max Speed':<15}{'Current Speed':<18}{'Distance':<15}")
        print("-" * 75)

        for c in self.cars:
            print(f"{c.reg:<15}{c.maxs:<15}{c.speed:<18}{c.distance:<15.1f}")

        print("-" * 75)

    def race_finished(self):
        for c in self.cars:
            if c.distance >= self.distance:
                return True

        return False


cars = []

for i in range(1, 11):
    maxs = random.randint(100, 200)
    reg = f"ABC-{i}"
    cars.append(car(reg, maxs))


race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()

print("\nRACE FINISHED!")
print(f"Total racing time: {hours} hours")

race.print_status()