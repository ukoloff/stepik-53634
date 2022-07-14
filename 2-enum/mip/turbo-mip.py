from mip import *

m = Model(solver_name=CBC)

ts = m.add_var_tensor((3, 5), 'turbines')

X = [2, 4, 7]
for i, N in enumerate(X):
  m.add_constr(sum(ts[i]) <= X[i], f"Type_{i}")

speeds = [3, 4, 5]
tss = np.array(speeds).reshape(-1, 1) * ts

Y = [6, 7, 8, 9, 10]
for j, N in enumerate(Y):
  m.add_constr(sum(tss[:, j]) <= N, f'Dist_{j}')

m.objective = ts.sum()
m.sense = MAX
m.write('turbo.mip.lp')
m.optimize()
