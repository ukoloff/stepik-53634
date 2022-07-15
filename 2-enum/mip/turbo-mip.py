from mip import Model
import numpy as np

max_by_type =[4, 7, 2]
max_by_dist = [5, 3, 10, 2, 4]
speed_by_type = [9, 7, 13]
max_sum = [150, 200, 350, 40, 120]

m = Model(solver_name='CBC')

ts = m.add_var_tensor((3, 5), 'T', var_type='I')

for i, N in enumerate(max_by_type):
  m.add_constr(sum(ts[i]) <= N, f"Type_{i+1}")

for j, N in enumerate(max_by_dist):
  m.add_constr(sum(ts[:, j]) <= N, f"Dist_{j+1}")

tss = ts * np.array(speed_by_type)[:, None]

for j, N in enumerate(max_sum):
  m.add_constr(sum(tss[:, j]) <= N, f'Sum_{j+1}')

m.objective = tss.sum()
m.sense = 'MAX'
m.verbose = 0

m.write('turbo.mip.lp')

m.optimize()
print("Status =", m.status)

counts = np.vectorize(lambda z: int(z.x))(ts)
print(counts)
for ax in range(2):
  print(*counts.sum(axis=ax))
