import math

def Compute(n, i):
    return ''.join([str(n * j) for j in range(1, i + 1)])

def Run():
    digits = set([str(i) for i in range(1, 10)])
    maximum = 0
    for i in range(2, 10):
        lower = int(math.pow(10, 9 / i - 1))
        upper = int(math.pow(10, 9 / i))
        while int(abs(upper  - lower)) > 1:
            if len(Compute((lower + upper) / 2, i)) < 9:
                lower = (lower + upper) / 2
            if len(Compute((lower + upper) / 2, i)) >= 9:
                upper = (lower + upper) / 2
        j = lower
        test = Compute(j, i)
        while len(test) < 10:
            if len(test) == 9 and set([k for k in test]) == digits: 
                if int(test) > maximum:
                    maximum = int(test) 
            j += 1
            test = Compute(j, i)
    print maximum

if __name__ == "__main__":
    Run()
