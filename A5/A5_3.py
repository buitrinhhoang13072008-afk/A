
def is_prime(n):
    if n< 2:
        return False
    if n == 2:
        return True
    if n %2 == 0:
        return False
    i = 3
    while i* i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


n = int(input("Enter an int: "))

if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")
