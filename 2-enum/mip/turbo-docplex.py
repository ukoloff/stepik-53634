from docplex.mp.model import Model
import numpy as np

m = Model(name='Turbo')
m.init_numpy()

shape = (3, 5)
ts = m.integer_var_matrix(*shape, name='turbines')
ts = np.array(list(ts.values())).reshape(shape)
# print(ts)

X = [2, 4, 7]
for i, N in enumerate(X):
  m.add_constraint(sum(ts[i]) <= N, f"Type_{i}")

speeds = [3, 4, 5]
tss = np.array(speeds).reshape(-1, 1) * ts

Y = [6, 7, 8, 9, 10]
for j, N in enumerate(Y):
  m.add_constraint(sum(tss[:, j]) <= N, f'Dist_{j}')

m.maximize(tss.sum())

m.export_as_lp(path='.', basename='turbo.docplex')
