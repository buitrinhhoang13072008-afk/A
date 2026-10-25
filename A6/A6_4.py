def sum(a):
    s = 0
    for i in range (len(a)):
        s+= a[i]
    return s

a = int(input("how many number do you want"))
res = []
for i in range(a):
    n = int(input("enter number"))
    res.append(n)
print(sum(res))