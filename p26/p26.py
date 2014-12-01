
def NumRepeatingDigits(denom):
    """Compute numer of repeating digits in 1 / denom."""
    decplace = 0
    dividend = 1
    remainders = {}
    while True:
        dividend *= 10
        quotient = dividend / denom
        remainder = dividend - (quotient * denom)
        if remainder in remainders:
            return decplace - remainders[remainder]
        remainders[remainder] = decplace
        decplace += 1
        



def Run():
    maximum = 0
    for i in range(999, 0, -1):
        if i < maximum:
            break
        if i % 10 == 0:
            continue
        res = NumRepeatingDigits(i)
        if res > maximum:
            maximum = res
            val = i
    print maximum
    print val
        
if __name__=="__main__":
    Run()
