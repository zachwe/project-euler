import math
import time

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n_distinct = [0, 0]

def num_distinct_primes(n):
    n_unique = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            n_unique += 1
            while n % i == 0:
                n /= i
            return n_unique + n_distinct[n]
    return 1

def run():
    consecutive = 0
    n = 2
    while True:
        n_primes = num_distinct_primes(n)
        n_distinct.append(n_primes)
        if n_primes == 4:
            consecutive += 1
            if consecutive == 4:
                return n - 3
        else:
                consecutive = 0
        n += 1

if __name__ == "__main__":
    start = time.time()
    out = run()
    end = time.time()
    print out
    print end- start

