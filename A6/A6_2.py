import random
m=int(input("enter the number"))
n = random.randint(1,m)
while (n!= m):
    print(n)
    n = random.randint(1,m)
print(n)