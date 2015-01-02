import collections

def checkDigits(x):
    mults = [str(x * i) for i in range(2, 7)]
    digits = collections.Counter(str(x))
    return all(map(lambda n: digits == collections.Counter(n), mults))

def Run():
    ndigits = 2
    i = 10 ** (ndigits - 1)
    res = False
    while True:
        res = checkDigits(i)
        if res:
            break
        i += 1
        if len(str(i)) > ndigits:
            ndigits += 1
            i = 10 ** (ndigits - 1)
    return i

if __name__ == "__main__":
    print Run()
