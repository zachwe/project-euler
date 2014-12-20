import sys

def SelfPower(power, digits=10):
    """Returns the last 10 digits of i**i"""
    mod = 10 ** digits
    res = 1
    for i in range(power):
        res = res * power % mod
    return res

def Run(digits, ceiling=1001):
    return sum([SelfPower(i, digits=digits) for i in range(1, ceiling)]) % (10 ** digits)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        digits = int(sys.argv[1])
    else:
        digits = 10
    if len(sys.argv) > 2:
        ceiling = int(sys.argv[2])
        print Run(digits=digits, ceiling=ceiling)
    else:
        print Run(digits=digits)
