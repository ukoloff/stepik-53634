import numpy as np


def bits2(n):
    """
    Precalculate table with 2 sequential bits == 0
    """
    table = np.zeros(2 ** n, dtype=bool)
    table[-1] = 1

    pair = 3
    for i in range(1, n):
        for j in range(pair, len(table)):
            if not table[j]:
                continue
            if j & pair != pair:
                continue
            table[j ^ pair] = 1
        pair <<= 1
    return table


def tile(n, m, k=0):
    if n > m:
        n, m = m, n
    b2 = bits2(n)

    counts = [0] * 2 ** n
    counts[0] = 1

    for i in range(m):
        layer = [0] * len(counts)
        for p, N in enumerate(counts):
            if N == 0:
                continue
            for q in range(len(layer)):
                if p & q == 0 and b2[p ^ q]:
                    layer[q] += N
                    if k != 0:
                      layer[q] %= k
        counts = layer
    return counts[0]


print(tile(3, 2))
print(tile(5, 6))
print(tile(5000, 6) % 1000000000)
# print(tile(16, 16, 1000000000))
