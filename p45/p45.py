
def Run():
    triangle = lambda n: n * (n + 1) / 2
    pentagonal = lambda n: n * (3 * n - 1) / 2
    hexagonal = lambda n: n * (2 * n - 1)
    hstart = 144
    pstart = 166
    tstart = 286
    (hval, pval, tval) = (hexagonal(hstart), 
                            pentagonal(pstart),
                            triangle(tstart))
    while not (hval == pval and pval == tval):
        (hval, pval, tval) = (hexagonal(hstart), 
                              pentagonal(pstart),
                              triangle(tstart))
        minimum = min(hval, pval, tval)
        if minimum == hval:
            hstart += 1
        if minimum == pval:
            pstart += 1
        if minimum == tval:
            tstart += 1
    print tval, hval, pval

if __name__ == '__main__':
    Run()
