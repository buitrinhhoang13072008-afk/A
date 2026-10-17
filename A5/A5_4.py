print("you will be naming 5 cities")
n=0
a=[]
for i in range(1,6):
    name = input(f"this is the {i} city ")
    a.append(name)
for name in a:
    print(name)