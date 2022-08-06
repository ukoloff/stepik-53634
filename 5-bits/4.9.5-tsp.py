def read(filename):
    with open(filename) as f:
        return [[int(z) for z in f.readline().strip().split()]
                for i in range(int(f.readline()))]


def TSP(W):
    ...


TSP(read('salesman0.in'))
TSP(read('salesman2.in'))
