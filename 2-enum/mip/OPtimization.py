from docplex.mp.model import Model
m = Model(name = 'AirTurbines')
#from docplex.mp.model import *

# Variables

turbines = m.integer_var_matrix(keys1=3, keys2=5, name='turbines')

max_by_type =[4, 7, 2]
max_by_dist = [5, 3, 10, 2, 4]
speed_by_type = [9, 7, 13]
max_sum = [150, 200, 350, 40, 120]

for i, N in enumerate(max_by_type):
    m.add_constraint(sum(turbines[i, j] for j in range(5)) <= N)

for j, N in enumerate(max_by_dist):
    m.add_constraint(sum(turbines[i, j] for i in range(3)) <= N)

for j, N in enumerate(max_sum):
    m.add_constraint(sum(turbines[i, j] * speed_by_type[i] for i in range(3)) <= N)

m.maximize(sum(turbines[i, j] * speed_by_type[i] for i in range(3) for j in range(5)))

m.export_as_lp(path='.', basename='XXX')

sol = m.solve()
sol.display()

print(*(sum(turbines[i, j].sv for j in range(5)) for i in range(3)))
print(*(sum(turbines[i, j].sv for i in range(3)) for j in range(5)))
exit()

# Number of Turbines Variables
size1_turbines = m.integer_var(name = 'turbinesA')
size2_turbines = m.integer_var(name = 'turbinesB')
size3_turbines = m.integer_var(name = 'turbinesC')

# Optimal Speed of Typesized Turbines Constants
size1_sp = 9
size2_sp = 7
size3_sp = 13
# Average Districts' Airspeed Constants
district1_sp = 10
district2_sp = 7
district3_sp = 12
district4_sp = 4
district5_sp = 16

# Constraints
# Number of Typesized Turbines Constraints
size1_turbinesconstraint = m.add_constraint(size1_turbines <= 4)
size2_turbinesconstraint = m.add_constraint(size2_turbines <= 7)
size3_turbinesconstraint = m.add_constraint(size3_turbines <= 2)
# Number of Total Turbines Constraints
district1_total = m.add_constraint((size1_turbines + size2_turbines + size3_turbines) <= 5)
district2_total = m.add_constraint((size1_turbines + size2_turbines + size3_turbines) <= 3)
district3_total = m.add_constraint((size1_turbines + size2_turbines + size3_turbines) <= 10)
district4_total = m.add_constraint((size1_turbines + size2_turbines + size3_turbines) <= 2)
district5_total = m.add_constraint((size1_turbines + size2_turbines + size3_turbines) <= 4)
# District Capacity Constraints
totaldistrict1capacity_constraint = m.add_constraint(m.sum(size1_turbines * size1_sp) <= 150)
totaldistrict2capacity_constraint = m.add_constraint(m.sum(size1_turbines * size1_sp) <= 200)
totaldistrict3capacity_constraint = m.add_constraint(m.sum(size1_turbines * size1_sp) <= 350)
totaldistrict4capacity_constraint = m.add_constraint(m.sum(size1_turbines * size1_sp) <= 40)
totaldistrict5capacity_constraint = m.add_constraint(m.sum(size1_turbines * size1_sp) <= 120)

# Goals/Objs
m.maximize(size1_turbines * size1_sp + size2_turbines * size2_sp + size3_turbines * size3_sp)

sol = m.solve()
sol.display()