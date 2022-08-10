from functools import lru_cache


def tiles(n, m, k):
    @lru_cache(None)
    def go(n, mask):
        return (int(not mask + 1 & mask) if n == 0
                else sum(go(n - 1, x) for x in step(mask)) % k)

    m, n = sorted((n, m))
    return go(n, (1 << m + 1) - 1)


@lru_cache(None)
def step(mask):
    return ([1] if mask == 1
            else [2] if mask == 3
            else [x << 1 | ~mask & 1 for x in step(mask >> 1)] if mask & 3 < 3
            else [x << 2 | 3 for x in step(mask >> 2)] +
                 [x << 1 for x in step(mask >> 1)])


print(tiles(3, 2, 10))
print(tiles(5, 6, 1000000000))
# print(tiles(5000, 6, 1000000000))
print(tiles(16, 16, 1000000000))
