a = []
while True:
    n = input("please input numbers: ")
    if n == "":
        break
    a.append(float(n))
if a:
    print(f"min is {min(a)} and max is {max(a)}")