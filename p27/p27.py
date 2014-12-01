"""Solve freaking prob 27"""
import math

# Prime number thm: density of primes is like 1 / ln(n)  and since ln(1000) =
# 7ish which means there are
# probably like 150 or fewer primes under 1000

# for n^2 + an + b
# b must be prime or f(n=0) will not be prime.
# also, n = b - a will not be prime because n(b - a) + an + b = bn - an + an +
# b = bn + b = b (n + 1)


def is_prime(candidate):
    """returns true if is prime else false"""
    for i in range(2, int(math.sqrt(candidate)) + 1):
        if candidate % i == 0:
            return False
    return True

def GetStreak(a, b):
    streak = 0
    function = lambda n: (n ** 2) + (a * n) + b
    val = function(streak)
    while val > 0 and is_prime(val):
        streak += 1
        val = function(streak)
    return streak

def Run():
    best = (1, 41)
    beststreak = 0
    for b in range(0, 1000):
        if not is_prime(b):
            continue
        for a in range(-999, 1000):
            streak = GetStreak(a, b)
            if streak > beststreak:
                beststreak = streak
                best = (a, b)
    print best
    print beststreak
    print best[0] * best[1]
