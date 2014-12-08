import math

facs = [math.factorial(i) for i in range(10)]
total = 0
for i in range(3, facs[9] * 7):
    facsum = sum([facs[int(j)] for j in str(i)])
    if facsum == i:
        total += facsum
print total
