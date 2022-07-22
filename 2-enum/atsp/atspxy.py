# ATSPxy
from mip import Model, BINARY
import numpy as np

valueOf = np.vectorize(lambda z: z.x)

def read(filename):
    with open(filename) as f:
        return np.array([[int(z) for z in f.readline().strip().split()]
                         for i in range(int(f.readline()))])


def model(weights):
    m = Model(solver_name='CBC', name='Cycle Cover')
    X = m.add_var_tensor(weights.shape, var_type=BINARY, name='x')
    Y = m.add_var_tensor(weights.shape, name='y')

    m.sense = 'MIN'
    m.verbose = False
    m.objective = (z * X).sum()
    for v in X.diagonal():
      m += v == 0
    for axis in range(2):
      for v in X.sum(axis=axis):
        m += v == 1
    for i in range(1, Y.shape[0]):
      for j in range(1, i):
        if i == j:
          continue
        m += Y[i, j] >= X[i, j]
        m += Y[j, i] >= X[j, i]
        m += Y[i, j] + Y[j, i] == 1
        for k in range(1, j):
          m += Y[i, j] + Y[j, k] + Y[k, i] <= 2
    # m.write('atsp.lp')
    return m, X

def dump_tours(X):
  z = dict(np.argwhere(valueOf(X)))
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
