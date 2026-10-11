import random
a = random.randint(1,10)
n = int(input("please input number"))
while (a != n):
    if a > n:
        print("too low")
    else:
        print("too high")
    n = int(input("please input number"))
print(f"congrats your number is {a}")