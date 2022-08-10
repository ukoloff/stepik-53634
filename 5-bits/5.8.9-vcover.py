import numpy as np

f = open('new0.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, m = readi()
edges = [readi() for i in range(m)]

