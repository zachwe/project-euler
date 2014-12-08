# I'm going to solve this extremely stupidly because I'm tired.
import math

def IsPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def IsCircularPrime(n):
    s = str(n)
    for i in range(len(s)):
        if not IsPrime(int(s)):
            return False
        # rotate s
        s = s[len(s) - 1:] + s[:len(s) - 1]
    return True

def Run():
    answer = sum([1 for i in range(2, 1000000) if IsCircularPrime(i)])
    print answer

if __name__ == '__main__':
    Run()
