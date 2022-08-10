import numpy as np

f = open('friends2.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, m = readi()
edges = [readi() for i in range(m)]

cliques = np.zeros(2 ** n, dtype=bool)
visited = np.zeros(2 ** n, dtype=bool)
masks = 2 ** np.arange(n)

for a, z in edges:
    cliques[1 << a - 1 | 1 << z - 1] = 1

for i in range(2, len(cliques)):
    if not cliques[i]:
        continue
    for m in masks:
        if m & i:
            continue
        mask2 = m | i
        if visited[mask2]:
            continue
        visited[mask2] = 1
        cliques[mask2] = all(cliques[mask2 ^ z] for z in masks if z & mask2)


def count_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


size = max(count_bits(i) for i in np.nonzero(cliques)[0])
print(size)
