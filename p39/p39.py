
def Run():
    maxsols = 0
    pformaxsols = 0
    for p in range(1, 1001):
        solutions = 0
        for c in range(p / 2, p / 3, -1):
            aplusb = p - c
            for a in range(1, aplusb / 2 + 1):
                b = aplusb - a
                if a ** 2 + b ** 2 == c ** 2:
                    solutions += 1
        if solutions > maxsols:
            maxsols = solutions
            pformaxsols = p
    print maxsols
    print pformaxsols

if __name__ == '__main__':
    Run()

