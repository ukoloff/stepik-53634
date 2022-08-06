f = open('rucksack.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, W = readi()
items = [readi() for i in range(n)]


def knapsack(W, items):
    z = [0] * (W + 1)
    for w, c in items:
        for i in range(W, w - 1, -1):
          z[i] = max(z[i], z[i - w] + c)
    return z[-1]

print(knapsack(W, items))
