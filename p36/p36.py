
def Run():
    palindrome = lambda s: s == s[::-1]
    s = 0
    for i in range(1000000):
        if palindrome(str(i)) and palindrome(str(bin(i))[2:]):
            s += i
    print s

if __name__ == '__main__':
    Run()
