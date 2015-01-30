num, denom = 1, 2
counter = 0
for i in range(1000):
    if len(str(num + denom)) > len(str(denom)):
        counter += 1
    num, denom = denom, 2 * denom + num
print counter
