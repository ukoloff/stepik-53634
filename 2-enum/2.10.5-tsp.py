# f = open('tsp.in')
f = open('salesman.in')

W = [[int(z) for z in f.readline().strip().split()]
     for i in range(int(f.readline()))]

print(W)
