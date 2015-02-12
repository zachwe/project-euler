import time
import math
import itertools as it

primes = {}
def is_prime(n):
    if n in primes:
        return primes[n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            primes[n] = False
            return False
    primes[n] = True
    return True

def count_primes(base, replace_digs):
    foundation = []
    primes = []
    base_index = 0
    ndigits = len(base) + len(replace_digs)
    for i in range(ndigits):
        if str(i) in replace_digs:
            foundation.append(False)
        else:
            foundation.append(base[base_index])
            base_index += 1
    for d in range(10):
        test = ''.join([str(d) if not foundation[i] else foundation[i] for i in
                            range(ndigits)])
        if int(test[0]):
            test = int(test)
        else:
            continue
        if is_prime(test):
            primes.append(test)
    return primes

def main():
    candidates = []
    for ndigits in it.count(1):
        if candidates:
            break
        print ndigits
        digits = ''.join([str(d) for d in range(10)])
        for nstatic in range(1, ndigits):
            nreplaced = ndigits - nstatic
            for base in it.product(digits, repeat=nstatic):
                val = int(base[nstatic - 1])
                if val % 2 == 0:
                    continue
                places = ''.join([str(d) for d in range(ndigits)])
                for replace_digs in it.combinations(places, nreplaced):
                    primes = count_primes(base, replace_digs)
                    if len(primes) > 6:
                        if len(primes) > 7:
                            candidates.append(primes[0])
                        print primes
    return min(candidates)

if __name__ == "__main__":
    start = time.time()
    res = main()
    end = time.time()
    print res
    print end - start
