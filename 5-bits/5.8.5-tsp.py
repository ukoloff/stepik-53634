import numpy as np


def read(filename):
    with open(filename) as f:
        return np.array([[int(z) for z in f.readline().strip().split()]
                         for i in range(int(f.readline()))])


def TSP(W):
    N = len(W)
    dist = np.zeros((2 ** (N-1), N))
    prev = np.full_like(dist, -1, dtype=int)

    prev[0, 0] = 0

    for mask in range(len(dist)):
        for Z in range(N):
            if prev[mask, Z] < 0:
                continue
            D = dist[mask, Z]
            for A in range(1, N):
                if mask & 1 << A - 1:
                    continue
                mask2 = mask | 1 << A - 1
                D2 = D + W[Z, A]
                if prev[mask2, A] < 0 or dist[mask2, A] > D2:
                    dist[mask2, A] = D2
                    prev[mask2, A] = Z
    solution = min((dist[-1, i] + W[i, 0], i)
                   for i in range(1, N) if prev[-1, i] > 0)
    # Backtracking
    mask = prev.shape[0] - 1
    city = solution[1]
    tour = []
    while mask != 0:
        tour.append(city)
        mask, city = mask ^ 1 << city - 1, prev[mask, city]
    if tour[0] > tour[-1]:
        tour.reverse()
    print(solution[0])
    print(0, *tour)


TSP(read('salesman0.in'))
TSP(read('salesman2.in'))
