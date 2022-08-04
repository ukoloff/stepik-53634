from operator import itemgetter
f = open('lis.in')

f.readline()
seq = [int(z) for z in f.readline().split()]


def lis(seq):
    def my_max(lst):
        if len(lst) == 0:
            return [0, 1]
        maximum = max(z[0] for z in lst)
        return [maximum, sum(z[1] for z in lst if z[0] == maximum)]

    L = []
    for n in seq:
        z = my_max([z for i, z in enumerate(L) if seq[i] < n])
        z[0] += 1
        L.append(z)
    return my_max(L)


print(lis(seq))
