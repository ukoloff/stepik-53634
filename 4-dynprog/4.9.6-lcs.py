f = open('seq0.in')


def read():
    f.readline()
    return [int(z) for z in f.readline().split()]


a, b = read(), read()


def lcs(a, b):
    ...
