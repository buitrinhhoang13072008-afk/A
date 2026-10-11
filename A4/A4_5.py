username = "python"
password = "rule"
num = 1
u = input("please input username: ")
p = input("please input password: ")
while (u != username or p != password) and num <5:
    print("wrong")
    u = input("please input username: ")
    p = input("please input password: ")
    num += 1
if (num == 5 and u!= username and p!= password):
    print("acces denied")
else:
    print("welcome")