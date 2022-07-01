from random import shuffle

# f = open('tsp.in')
f = open('salesman.in')
# f = open('tsplib/br17.tsp')

W = [[int(z) for z in f.readline().strip().split()]
     for i in range(int(f.readline()))]


def TSP(W):
    tour = [0]
    nodes = [*range(1, len(W))]
    used = [0] * len(nodes)
    shuffle(nodes)
    bestW = None
    bestTour = None
    cuts = [0, None]

    def rec(w=0):
        if len(tour) > 1:
            w += W[tour[-2]][tour[-1]]
        if bestW is not None and bestW < w:
            cuts[0] += 1
            if cuts[1] is None or cuts[1] > len(tour):
              cuts[1] = len(tour)
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
        if bestW is None or (w, tour) < (bestW, bestTour):
            bestW, bestTour = w, tour[:]
            # print(bestW, end='\t', flush=True)

    print(bestW)
    print(*bestTour)
    print('// cuts:', cuts[0], 'len >=', cuts[1])
    print('// branches:', branches)

TSP(W)
