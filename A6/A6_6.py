def cal(a,b):
    area = (a/2)**2*3.14
    return area / b

s=0
for i in range (2):
    n = int(input("input pizza diameter"))
    m = int(input("input pizza price"))
    if (cal(n,m) > s):
        s=cal(n,m)
print(f"The best pizza value is: {s:.2f} sq units per currency unit")