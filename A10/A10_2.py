class Elevator():
    def __init__(self,highest_floor,lowest_floor):
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.current_floor = lowest_floor
        self.target_floor = 0
    def floor_up(self):
        while self.current_floor < self.target_floor:
            self.current_floor += 1
            print(f"This is floor {self.current_floor}")

    def floor_down(self):
        while self.current_floor > self.target_floor:
            self.current_floor -= 1
            print(f"This is floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.lowest_floor or target_floor > self.highest_floor:
            print("Invalid floor!")
            return

        self.target_floor = target_floor

        if self.current_floor < self.target_floor:
            self.floor_up()

        elif self.current_floor > self.target_floor:
            self.floor_down()
class Building:
    def __init__(self, lowest_floor, highest_floor, number_of_elevators):
        self.elevators = []

        for i in range(number_of_elevators):
            elevator = Elevator(highest_floor, lowest_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Invalid elevator number!")
            return

        self.elevators[elevator_number - 1].go_to_floor(destination_floor)


building = Building(0, 10, 3)

building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.run_elevator(3, 3)

building.run_elevator(1, 0)