# MTZ: Miller et al.
from mip import Model, BINARY
import numpy as np

valueOf = np.vectorize(lambda z: z.x)

def read(filename):
    with open(filename) as f:
        return np.array([[int(z) for z in f.readline().strip().split()]
                         for i in range(int(f.readline()))])


def model(weights):
    m = Model(solver_name='CBC', name='MTZ')
    X = m.add_var_tensor(weights.shape, var_type=BINARY, name='x')
    Y = m.add_var_tensor(weights.shape[:1], name='y')

    m.sense = 'MIN'
    m.verbose = False
    m.objective = (z * X).sum()
    for v in X.diagonal():
      m += v == 0
    for axis in range(2):
      for v in X.sum(axis=axis):
        m += v == 1
    N = len(Y)
    for i in range(1, N):
      for j in range(1, N):
        if i == j:
          continue
        m += Y[i] - Y[j] + (N - 1) * X[i, j] <= N - 2
    # m.write('mtz.lp')
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
