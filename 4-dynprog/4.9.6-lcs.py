import numpy as np
f = open('seq2.in')


def read():
    f.readline()
    return [int(z) for z in f.readline().split()]


a, b = read(), read()


def lcs(a, b):
    Z = np.zeros((len(a) + 1, len(b) + 1), dtype=int)
    for i, ca in enumerate(a):
      for j, cb in enumerate(b):
        Z[i+1, j+1] = max(Z[i, j+1], Z[i+1, j])
        if ca == cb:
          Z[i+1, j+1] = max(Z[i+1, j+1], Z[i, j] + 1)
    return Z[-1, -1]

print(lcs(a, b))
