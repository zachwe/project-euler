
n = 1
for i in range(7830457):
    n << 1
    n %= int(1e10)
n *= 28433
n %= int(1e10)
print n + 1
