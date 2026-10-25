def convert(n):
    return n *4.54609
while True:
    n = float(input("enter gallon"))
    if(n < 0):
        break
    print(f"{convert(n)} liters")