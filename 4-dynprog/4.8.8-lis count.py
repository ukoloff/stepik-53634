from operator import itemgetter
f = open('lis.in')

f.readline()
seq = [int(z) for z in f.readline().split()]


def lis(seq):
    def my_max(lst, add=0):
        if len(lst) == 0:
            return (add, 1)
        maximum = max(z[0] for z in lst)
        return (maximum + add, sum(z[1] for z in lst if z[0] == maximum))

    L = []
    for n in seq:
        L.append(my_max([z for i, z in enumerate(L) if seq[i] < n], add=1))
    return my_max(L)


print(lis(seq))
