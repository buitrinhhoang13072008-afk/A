a=[]
n= input("please intput your number")
while (n):
    n = int(n)
    a.append(n)
    n= input("please intput your number")
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i])
