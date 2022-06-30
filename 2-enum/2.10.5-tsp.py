from random import shuffle

# f = open('tsp.in')
f = open('salesman.in')

W = [[int(z) for z in f.readline().strip().split()]
     for i in range(int(f.readline()))]


def TSP(W):
    tour = [0]
    nodes = [*range(1, len(W))]
    used = [0] * len(nodes)
    # shuffle(nodes)
    bestW = None
    bestTour = None
    cuts = []

    def rec(w=0):
        if len(tour) > 1:
            w += W[tour[-2]][tour[-1]]
        if bestW is not None and bestW < w:
            cuts.append(tour)
            return
        if len(tour) == len(W):
            yield w + W[tour[-1]][tour[0]]
            return
        for i in range(len(nodes)):
            if used[i]:
                continue
            used[i] = 1
            tour.append(nodes[i])
            yield from rec(w)
            used[i] = 0
            tour.pop()

    branches = 0
    for w in rec():
        branches += 1
        if bestW is None or w < bestW:
            bestW = w
            bestTour = tour[:]

    print(bestW)
    print(*bestTour)
    print('// cuts:', len(cuts))
    print('// branches:', branches)

TSP(W)
