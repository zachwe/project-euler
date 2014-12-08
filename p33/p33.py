import math

def ShareDigit(num, denom):
    c1 = (num / 10 == denom % 10 or num % 10 == denom / 10 
        or num / 10 == denom / 10
        or num % 10 == denom % 10)
    c2 = num % 10 != 0 and denom % 10 != 0
    if c1 and c2:
        numdigs = ''.join([i for i in str(num) if i not in str(denom)])
        denomdigs = ''.join([i for i in str(denom) if i not in str(num)])
        if numdigs and denomdigs:
            return (int(numdigs), int(denomdigs))
    return False
def Reduce(num, denom):
    for i in range(2, int(math.sqrt(num) + 1)):
        while num % i == 0 and denom % i == 0:
            num /= i
            denom /= i
    return (num, denom)

def Run():
    # Brute force this bitch. Won't be tough I think.
    numprod, denomprod = 1, 1
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            digits = ShareDigit(numerator, denominator)
            if digits:
                q1 = round(float(numerator) / denominator, 4)
                q2 = round(float(digits[0]) / digits[1], 4)
                if q1 == q2:
                    print numerator
                    print denominator
                    numprod *= numerator
                    denomprod *= denominator
    reducednum, reduceddenom = Reduce(numprod, denomprod)
    print reduceddenom

if __name__ == "__main__":
    Run()
