import numpy as np

f = open('new2.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, m = readi()
edges = [readi() for i in range(m)]

friends = np.zeros(2 ** n, dtype=int)

for i in range(n):
    friends[1 << i] = 1 << i
for a, z in edges:
    friends[1 << a-1] |= 1 << z-1
    friends[1 << z-1] |= 1 << a-1

for i in range(1, len(friends)):
    if friends[i]:
        continue
    m = i & i - 1
    friends[i] = friends[m] | friends[m ^ i]


def count_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


size = min(count_bits(i) for i in np.nonzero(friends == len(friends) - 1)[0])
print(size)
