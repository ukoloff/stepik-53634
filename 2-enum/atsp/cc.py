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

def dump_tours(X):
  z = dict(np.argwhere(np.vectorize(lambda z: z.x)(X)))
  tour = []
  queue = set(z.keys())
  while len(queue):
    cycle = []
    tour.append(cycle)
    x = min(queue)
    while True:
      cycle.append(x)
      queue.remove(x)
      x = z[x]
      if x not in queue:
        break
  print(*tour)


# z = read('../tsp.in')
z = read('../salesman.in')
# z = read('../tsplib/br17.tsp')
# z = read('../tsplib/bayg29.tsp')
m, X = model(z)
m.optimize()
print('Len =', m.objective_value)
# print(X)
dump_tours(X)
