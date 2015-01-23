import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_twice_square(n):
    return n % 2 == 0 and int(math.sqrt(n / 2)) ** 2 == n / 2 

def primes_between(a, b):
    return [x for x in range(a + 1, b) if is_prime(x)]

def is_sum(n, primes):
    for p in primes:
        if is_twice_square(n - p):
            return True
    return False

def run():
    primes = [2]
    n = 3
    while True:
        if is_prime(n):
            primes.append(n)
            n += 2
            continue
        if not is_sum(n, primes):
            print primes
            print
            return n
        n += 2

if __name__ == "__main__":
    print run()
        
