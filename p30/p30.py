
# quick and dirty. let's do this. 
total = 0
for i in range(10, 420000):
    n = i
    tmptotal = 0
    while n:
        tmptotal += (n % 10) ** 5
        n = n / 10
    if tmptotal == i:
        print i
        total += i
print total


