class  sw2:
    ppl = {}
    def __init__(self,name,height):
        self.name = name
        self.height = height
        sw2.ppl[self.name] = self.height
    def check(self):
        if sw2.ppl:
            print(f"there are{len(sw2.ppl)} ppl")
    def tallest(self):
        tallest_name = max(sw2.ppl, key=sw2.ppl.get)
        print(f"The tallest is {tallest_name} with a height of {sw2.ppl[tallest_name]}.")
        sw2.ppl.pop(tallest_name)

    def show(self):
        print(self.name)
        print(self.height)

a = sw2("Alice", 170)
b = sw2("Bob", 185)
a.check()       # Output: There are 2 people.
a.tallest()     # Output: The tallest is Bob with a height of 185.
a.show()