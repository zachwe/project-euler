# above n=10, there are no powers n^a that are a digits, since every n^a has
# a + 1 digits
count = 0
for i in range(1, 10):
    n = 1
    while True:
        n_digits = len(str(i ** n))
        if  n_digits == n:
            count += 1
        elif n_digits < n:
            break
        n += 1

print count
