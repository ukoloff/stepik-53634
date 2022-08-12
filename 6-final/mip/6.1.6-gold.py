from docplex.mp.model import Model
import numpy as np

f = open('../gold3.in')

f.readline()
bars = np.array([int(z) for z in f.readline().split()])

m = Model(name='Gold')
m.init_numpy()

X = np.array(m.binary_var_list(len(bars), name='x'))

m.minimize(m.abs(bars.sum() - 2 * (bars * X).sum()))

sol = m.solve()
sol.display()
print(*(z.sv for z in X))
