from itertools import islice

def split(n, min=1, res=()):
    if n == 0:
        yield res
    for x in range(min, n + 1):
        yield from split(n - x, x, res + (x,))

# for z in islice(split(35), 13672-1, None):
#     print(z)
#     break

N = 10
print(*islice(split(7), N - 1, N))

N = 13672
print(*islice(split(35), N - 1, N))
