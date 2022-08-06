from enum import EnumMeta
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


for i in range(1, 5):
    print(*(f"{'+' if ok else '-'}{n:0{i}b}" for n, ok in enumerate(bits2(i))))
