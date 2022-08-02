from mip import Model
import numpy as np
from operator import attrgetter

coins = [10, 8, 6, 1]
target = 25

m = Model(solver_name='CBC')
m.name = 'Coins'
m.sense = 'MIN'
m.verbose = False

X = m.add_var_tensor((len(coins),), name='x', var_type='I')

m.objective = X.sum()
m += X.dot(coins) == target

m.optimize()
print(m.objective_value)
counts = np.vectorize(attrgetter('x'))(X)
print(counts)
