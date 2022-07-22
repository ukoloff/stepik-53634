# Cycle cover
from mip import Model, BINARY
import numpy as np


def read(filename):
    with open(filename) as f:
        return np.array([[int(z) for z in f.readline().strip().split()]
                         for i in range(int(f.readline()))])


def model(weights):
    m = Model(solver_name='CBC', name='Cycle Cover')
    X = m.add_var_tensor(weights.shape, var_type=BINARY, name='x')
    m.sense = 'MAX'
    m.verbose = False
    m.objective = (z * X).sum()
    for v in X.diagonal():
      m += v == 0
    for axis in range(2):
      for v in X.sum(axis=axis):
        m += v == 1
    # m.write('cc.lp')
    return m, X


z = read('../salesman.in')
m, X = model(z)
m.optimize()
X = np.vectorize(lambda z: z.x)(X)
print(X)
