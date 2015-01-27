import time
start = time.time()
def chain_end(n, memo):
    if n in memo:
        return memo[n]
    else:
        next_n = sum([int(d) * int(d) for d in str(n)])
        memo[n] = chain_end(next_n, memo)
        return memo[n]

chains = {89: 89, 1: 1}
vals = [True if i == 89 else False for i in range(1, 81 * 7 + 1)]
for i in range(81 * 7):
    vals[i] = chain_end(i + 1, chains) == 89
print vals
count = 0
for i in range(1, int(1e7)):
    next_link = 0
    while i > 0:
        next_link += (i % 10) ** 2
        i /= 10
    count += vals[next_link - 1]

end = time.time()
print count
print end - start
