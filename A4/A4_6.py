import random
num = int(input("please input number"))
res=0
for i in range (num):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2 <= 1):
        res += 1
print(f"the aproximate of pi is {res/num * 4}")
