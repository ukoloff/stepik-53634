f = open('lis.in')

f.readline()
seq = [int(z) for z in f.readline().split()]


def lis(seq):
    L = []
    for n in seq:
      L.append(1 + max([z for i, z in enumerate(L) if seq[i] < n], default=0))
    return max(L)


print(lis(seq))
