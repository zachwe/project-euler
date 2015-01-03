
def digitalSum(n):
    res = 0
    while n > 0:
        res += n % 10
        n /= 10
    return res

def run():
    res = max([a ** b for b in range(1, 101) 
        for a in range(2, 100) if a % 10 != 0], key=digitalSum)
    return digitalSum(res)

if __name__ == "__main__":
    print run()
