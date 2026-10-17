import random
n = int(input("input your number: "))
temp=0
for i in range(n):
    temp += random.randint(1, 6)
print(temp)