import math

def SumDivisors(num):
    total = 0
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            total += i
            if num / i != i:
                total += num / i
    total += 1
    return total

def Run():
    total = 0
    amicable = {}
    for i in range(2,10000):
        if i in amicable:
            continue
        sumone = SumDivisors(i)
        sumtwo = SumDivisors(sumone)
        # condition for amicability
        if sumtwo == i and sumone != i:
            total += i + sumone
            amicable[i] = sumone
            amicable[sumone] = i
    print total

if __name__ == '__main__':
    Run()
