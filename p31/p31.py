"""Solve problem 31"""

from datetime import datetime

# for each number of coins from 1 to 200, calculate the total number of
# combinations that use exactly that number. Use a model of bins and
# separators. (199 possible separator slots.)

def CountCombos(subset, summ):
    # loop thru the array from large to small
    # for i, s in enumerate(subset[::-1]):
    length = len(subset)
    target = subset[-1]
    total = 0
    ubound = summ / target
    for i in range(1, ubound + 1):
        # use i copies of s
        rem = summ - (i * target)
        # if we've added to summ but not used everything at least once,
        # return 0.
        if rem > 0 and length > 1:
            total += CountCombos(subset[:length - 1], rem)
        elif rem == 0 and length > 1:
            continue
        elif rem == 0 and length == 1:
            total += 1
    return total

        

def Run():
    start = datetime.now()
    # legal sized parts
    vals = [1,2, 5, 10, 20, 50, 100, 200]
    # what we're summing to
    total = 200
    ret = 0

    for i in range(1, 2 ** len(vals) - 1 + 1):
        # pick a non-empty sorted subset of vals
        subset = [vals[j] for j in range(len(vals))
                if i >> j & 1]
        ret += CountCombos(subset, total)
    end = datetime.now()
    print end - start
    print ret        


if __name__=='__main__':
    Run()
