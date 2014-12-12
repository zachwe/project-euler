import re

def IsTriangleWord(word):
    score = sum([ord(w)  - ord("A") + 1 for w in word])
    lower = int((score * 2) ** 0.5)
    print lower
    if lower * (lower + 1) == 2 * score:
        return 1
    return 0

def Run():
    with open('p042_words.txt', 'rb') as words:
        wl = words.read().split(",")
        regexp = r'"(\w+)"'
        wl = [re.match(regexp, w).group(1) for w in wl]
        print wl[0]
        sol = sum([IsTriangleWord(w) for w in wl])
        return sol

if __name__ == '__main__':
    print Run()
