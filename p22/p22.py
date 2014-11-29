import re

def Run():
    scoreletter = lambda x: ord(x) - ord('A') + 1
    scoreword = lambda w: sum([scoreletter(l) for l in w])
    scorename = lambda i, n: (i + 1) * scoreword(n)
    regex = r'"(\w+)"'
    with open('p022_names.txt', 'rb') as fnames:
        names = fnames.read().split(',')
        clippednames = map(lambda x: re.match(regex, x).group(1), names)
        clippednames = sorted(clippednames)
        total = sum([scorename(i, name) for i, name in enumerate(clippednames)])

        print total
