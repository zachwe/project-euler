
def Run():
    fib, fibprev = 1, 1
    i = 2
    while len(str(fib)) < 1000:
        fib, fibprev = fibprev + fib, fib
        i += 1
    print i
