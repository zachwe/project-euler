import itertools

def Run():
    digits = [str(i) for i in range(1, 10)]
    out = []
    for i in itertools.permutations(digits):
        digstring = ''.join(i)
        left = digstring[:5]
        right = int(digstring[5:])
        for j in range(1, 4):
            t1 = int(left[:j])
            t2 = int(left[j:])
            if t1 * t2 == right:
                out.append(right)
    res = sum(list(set(out)))
    return res
