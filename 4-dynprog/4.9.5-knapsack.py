f = open('rucksack.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, W = readi()
items = [readi() for i in range(n)]


def knapsack(W, items):
    z = [0] * (W + 1)
    last = [None] * (W + 1)
    for item, (w, c) in enumerate(items):
        for i in range(W, w - 1, -1):
            if z[i] < z[i - w] + c:
                z[i] = z[i - w] + c
                # last[i] = item
                prev = last[i - w]
                if prev is None:
                  prev = []
                last[i] = [*prev, item + 1]
    # result = []
    # i = W
    # while i > 0 and last[i] >= 0:
    #   result.append(last[i] + 1)
    #   i -= items[last[i]][0]
    # result.reverse()
    print(z[W])
    print(*last[W])


knapsack(W, items)
