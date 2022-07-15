from docplex.mp.model import Model
import numpy as np

max_by_type =[4, 7, 2]
max_by_dist = [5, 3, 10, 2, 4]
speed_by_type = [9, 7, 13]
max_sum = [150, 200, 350, 40, 120]

m = Model(name='Turbo')
m.init_numpy()

shape = (3, 5)
ts = m.integer_var_matrix(*shape, name='T')
ts = np.array(list(ts.values())).reshape(shape)

for i, N in enumerate(max_by_type):
  m.add_constraint(sum(ts[i]) <= N, f"Type_{i+1}")

for j, N in enumerate(max_by_dist):
  m.add_constraint(sum(ts[:, j]) <= N, f"Dist_{j+1}")

tss = ts * np.array(speed_by_type)[:, None]

for j, N in enumerate(max_sum):
  m.add_constraint(sum(tss[:, j]) <= N, f'Sum_{j+1}')

m.maximize(tss.sum())

m.export_as_lp(path='.', basename='turbo.docplex')

sol = m.solve()
print('Status =', sol.solve_details.status)
sol.display()

counts = np.vectorize(lambda x: int(x.sv))(ts)
print(counts)
for ax in range(2):
  print(*counts.sum(axis=ax))
