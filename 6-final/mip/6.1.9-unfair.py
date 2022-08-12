from mip import Model, xsum
import numpy as np

f = open('../gold4.in')

f.readline()
bars = np.array([int(z) for z in f.readline().split()])

m = Model(solver_name='CBC')
m.verbose = False

X = m.add_var_tensor(bars.shape, 'x', var_type='B')
m.add_constr(xsum(X) == bars.shape[0] // 2)

m.sense = 'MAX'
m.objective = bars.sum() - 2 * (bars * X).sum()

m.optimize()
print('OBJ =', m.objective_value)
print()
