import time
import math

def isPent(num):
    insidesqrt = 24 * num + 1
    sqrt = math.sqrt(insidesqrt)
    if int(sqrt) ** 2 == insidesqrt:
        if (sqrt + 1) % 6 == 0:
            return True

def run():
    n = 0
    gap = lambda n: 3 * n + 1
    pents = []
    while True:
        n += 1
        p_n = (n * (3 * n - 1)) / 2
        for pent in pents:
            if isPent(p_n - pent) and isPent(p_n + pent):
                return (p_n, pent)
        pents.append(p_n)
    return False



if __name__=='__main__':
    start = time.time()
    out = run()
    end = time.time()
    print out
    print end - start
