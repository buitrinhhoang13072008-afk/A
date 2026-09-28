num=1
while(num > 0):
    num = int(input("Enter a year:"))
    if (num %4 ==0):
        if(num % 100 ==0 and num % 400 ==0):
            print(f"{num} is a leap year")
            continue
        else:
            print(f"{num} is not a leap year")
            continue
        print(f"{num} is a leap year.")
    else:
        print(f"{num} is not a leap year")