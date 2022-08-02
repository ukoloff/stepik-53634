from mip import Model, BINARY
import numpy as np
from operator import attrgetter


def model(N):
    m = Model(solver_name='CBC', name='Queens')
    Q = m.add_var_tensor((N, N), var_type=BINARY, name='q')

    m.sense = 'MAX'
    m.verbose = False

    m.objective = Q.sum()

    for axis in range(2):
        for row in Q.sum(axis=axis):
            m += row <= 1

    for q in (Q, np.flipud(Q)):
        for i in range(2-N, N-1):
            m += q.trace(i) <= 1

    return m, Q


def out(Q):
    print(*np.vectorize(attrgetter('x'))(Q).nonzero())


for i in range(2, 9):
    m, Q = model(i)
    # m.write('q3.lp')
    m.optimize()
    print(i, int(m.objective_value))

out(Q)

m, Q = model(50)
m.optimize()
print(int(m.objective_value))

out(Q)
