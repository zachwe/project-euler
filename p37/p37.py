import math

def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def IsTruncatableRight(n):
    l = len(str(n))
    if l == 1:
        return IsPrime(n)
    else:
        return IsPrime(n) and IsTruncatableRight(n % int(math.pow(10, l - 1)))

def IsTruncatableLeft(n):
    if n < 10:
        return IsPrime(n)
    else:
        return IsPrime(n) and IsTruncatableLeft(n / 10)

def Run():
    i, found, total = 10, 0, 0
    while found < 11: 
        if IsTruncatableRight(i) and IsTruncatableLeft(i):
            print i
            total += i
            found += 1
        i += 1
    print total

if __name__ == "__main__":
    Run()
