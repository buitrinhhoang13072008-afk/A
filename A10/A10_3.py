class elevator():
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
h = elevator(10, 0)

h.go_to_floor(5)
h.go_to_floor(0)