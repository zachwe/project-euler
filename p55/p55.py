def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    for i in range(50):
        rev = int(str(n)[::-1])
        n += rev
        if is_palindrome(n):
            return False
    return True

print sum([1 for i in range(1, int(1e4)) if is_lychrel(i)])
