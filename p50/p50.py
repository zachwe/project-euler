import math

def PrimeSieve(n):
    ar = [True if i > 1 else False for i in range(n)]
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        for j in range(i**2, n, i):
            ar[j] = False
    
    primes = [i for i, b in enumerate(ar) if b]

    return primes

def FindStart(p, ar, chainlength, lower=0, upper=-1):
    """Find a candidate index to start the sum"""
    if upper == -1:
        upper = len(ar)
    guess = (upper - lower) / 2
    if (ar[guess] * chainlength < p 
            and (ar[guess + 1]* chainlength > p or guess + 1 >= len(ar))):
        return guess
    else:
        if ar[guess] < p:
            return FindStart(p, ar, chainlength, lower=lower, upper=guess)
        elif ar[guess] > p:
            return FindStart(p, ar, chainlength, lower=guess + 1, upper=upper)

def FindMaxSum(p, ar, goal=1):
    summation = 0
    lower = 0
    upper = 0
    while upper < len(ar) and summation  + ar[upper] <= p:
        summation += ar[upper]
        upper += 1
    if summation == p:
        return upper - lower
    
    while upper < len(ar) and summation < p:
        summation += ar[upper]
        upper += 1
        while summation > p:
            summation -= ar[lower]
            lower += 1
        if upper - lower < goal:
            return False
    if summation == p:
        return upper - lower
    return False


def Run():
    primes = PrimeSieve(1000000)
    maxsum = (0, 0)#(21, 953)
    # find the starting point
    for p in primes:
        candidate = FindMaxSum(p, primes, maxsum[0])
        if candidate and candidate > maxsum[0]:
            maxsum = (candidate, p)
    return maxsum

if __name__=='__main__':
    print Run()
