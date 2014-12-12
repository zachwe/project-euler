import math
import itertools

def isPrime(num):
    for n in xrange(2, int(num ** .5 + 1)):
        if num % n == 0:
            return False
    return True

def Run():
    maximum = 0
    for i in range(9, 1, -1):
        for perm in itertools.permutations(range(1, i + 1)):
            test = int(''.join([str(p) for p in perm]))
            if isPrime(test) and test > maximum:
                maximum = test
        if maximum > 0:
            return maximum

if __name__ == '__main__':
    print Run()
