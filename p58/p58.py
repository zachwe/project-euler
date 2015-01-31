import math
import time
start_time = time.time()
PRIME_CEIL = int(1e10)

def is_prime(x):
    if not x % 2:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

corner = 1
side_length = 1
num_prime_diags, num_diags = 0, 1
while num_prime_diags * 10 >= num_diags or not num_prime_diags:
    side_length += 2
    n_new_primes = sum(map(is_prime, [corner + i * (side_length - 1) for
                                    i in range(1, 5)]))
    num_prime_diags += n_new_primes
    num_diags += 4
    corner += 4 * (side_length - 1)

end_time = time.time()

print side_length
print end_time - start_time
