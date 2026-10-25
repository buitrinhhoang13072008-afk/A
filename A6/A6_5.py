def rem(a):
    for i in range(len(a) - 1, -1, -1):
        if (a[i] % 2 != 0):
            a.pop(i)
    return a

a = int(input("how many number do you want"))
res = []
for i in range(a):
    n = int(input("enter number"))
    res.append(n)
rem(res)
for i in range(len(res)):
    print(res[i])