import time
start = time.time()
ar = [True for i in range(int(1e4))]
for i in range(2, int(1e4)):
    if ar[i]:
        for j in range(2 * i, int(1e4), i):
            ar[j] = False

perm_primes = {}
for i, val in enumerate(ar[1000:]):
    if val:
        n = i + 1000
        key = ''.join(sorted(str(n)))
        if key in perm_primes:
            for i in perm_primes[key]:
                gap = n - i
                if (n + gap < int(1e4) and ar[n + gap] and
                        set(str(n + gap)) == set(str(n))):
                    print str(i) + str(n) + str(n + gap)
            perm_primes[key].append(n)
        else:
            perm_primes[key] = [n]
end = time.time()
print end - start
