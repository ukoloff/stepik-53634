f = open('rucksack.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, W = readi()
items = [readi() for i in range(n)]


def knapsack(W, items):
    z = [0] * (W + 1)
    paths = [None] * (W + 1)
    for item, (w, c) in enumerate(items):
        for i in range(W, w - 1, -1):
            if z[i] < z[i - w] + c:
                z[i] = z[i - w] + c
                # last[i] = item
                prev = paths[i - w]
                if prev is None:
                  prev = []
                paths[i] = [*prev, item + 1]
    print(z[W])
    print(*paths[W])


knapsack(W, items)
