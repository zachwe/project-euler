import datetime

def BuildPD():
    digits = set([str(i) for i in range(10)])
    current = []
    numdigs = 3
    for divisor in [17, 13, 11, 7, 5, 3, 2]:
        frontier = []
        candidates = [str(i) if len(str(i)) == 3 else "0" + str(i)
                      for i in range(divisor, 1000, divisor)]
        if not current:
            current = [str(c) for c in candidates 
                       if len(set([char for char in c])) == numdigs]
            continue
        for c in candidates:
            for curr in current:
                if (c[1:] == curr[:2] and 
                        len(set([char for char in c + curr])) == numdigs + 1):
                    frontier.append(c[0] + curr) 
        current = frontier
        numdigs += 1
    out = []
    for c in current:
        leftover = digits.difference(set([char for char in c]))
        lastdigit = list(leftover)[0]
        out.append(int(lastdigit + c))
    return sum(out)



def Run():
    start = datetime.datetime.now()
    out = BuildPD()
    end = datetime.datetime.now()
    print out
    print end - start


if __name__ == '__main__':
    Run()
