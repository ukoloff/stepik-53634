f = open('change.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, s = readi()
coins = readi()


def change(s, coins):
    n = [None] * (s + 1)
    n[0] = 0
    for coin in coins:
        for i, z in enumerate(n):
            if z is None:
                continue
            if i + coin >= len(n):
                continue
            if n[i + coin] is None or n[i + coin] > z + 1:
                n[i + coin] = z + 1
    return n[-1]


print(change(s, coins))
