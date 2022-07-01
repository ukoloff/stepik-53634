from random import shuffle


def read(filename):
    with open(filename) as f:
        return [[int(z) for z in f.readline().strip().split()]
                for i in range(int(f.readline()))]


factorial_cache = [1]


def factorial(n):
    for i in range(len(factorial_cache), n + 1):
        factorial_cache.append(i * factorial_cache[-1])
    return factorial_cache[n]


def TSP(W):
    tour = [0]
    N = len(W)
    problemSpace = factorial(N)
    nodes = [*range(1, N)]
    used = [0] * len(nodes)
    shuffle(nodes)
    bestW = None
    bestTour = None
    cuts = 0
    shortestCut = None
    cutBranches = 0

    def rec(w=0):
        if len(tour) > 1:
            w += W[tour[-2]][tour[-1]]
        if bestW is not None and bestW < w:
            nonlocal cuts, shortestCut, cutBranches
            cuts += 1
            cutBranches += factorial(N - len(tour))
            if shortestCut is None or shortestCut > len(tour):
                shortestCut = len(tour)
            return
        if len(tour) == N:
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
    print('// cuts:', cuts, 'len >=', shortestCut, 'branches =', cutBranches)
    print('// branches:', branches)


# TSP(read('tsp.in'))
TSP(read('salesman.in'))
# TSP(read('tsplib/br17.tsp'))
