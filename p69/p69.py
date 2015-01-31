def primes(n):
    sieve = [True if i >= 2 else False for i in range(n)]
    for i in range(2, n):
        if not sieve[i]:
            continue
        for j in range(2 * i, n, i):
            sieve[j] = False
    primes = [i for i, v in enumerate(sieve) if v]
    for p in primes:
        yield p
num = 1
for p in primes(int(1e6)):
    if num * p <= int(1e6):
        num *= p
    else:
        break
print num
