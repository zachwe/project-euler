import math

def choose(n, m):
    return int(math.factorial(n) / (math.factorial(m) * math.factorial(n - m)))

def Run():
    count = 0
    for n in range(100, 0, -1):
        m = n / 2
        v = choose(n, m)
        if v <= 1e6:
            return count
        else:
            if n % 2 == 0:
                count -= 1
            while v > 1e6:
                count += 2
                m -= 1
                v = choose(n, m)

if __name__ == "__main__":
    print Run()
