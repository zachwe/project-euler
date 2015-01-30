with open("p059_cipher.txt", "rb") as f:
    ascii_codes = [int(c) for c in f.read().strip().split(',')]
    max_letter_count = 0
    best_guess = None
    lower, upper = ord('a'), ord('z')
    for a in range(lower, upper + 1):
        for b in range(lower, upper + 1):
            for c in range(lower, upper + 1):
                key = (a, b, c)
                out = [val ^ key[i % 3] for i, val in enumerate(ascii_codes)]
                ascii_verifier = lambda x: (x >= 65 and x <= 122) or x == 32
                letter_count = sum(map(ascii_verifier, out))
                if letter_count > max_letter_count:
                    max_letter_count = letter_count
                    best_guess = out

    print ''.join(chr(i) for i in best_guess)
    print sum(best_guess)
            
