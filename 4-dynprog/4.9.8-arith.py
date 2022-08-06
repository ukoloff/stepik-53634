f = open('arithm2.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, x = readi()
numbers = readi()

target = (sum(numbers) - x) // 2

sums = [[]] + [None] * target

for i, a in enumerate(numbers):
    if i == 0:
        continue
    for j in range(target, a-1, -1):
        if sums[j] is not None:
            continue
        if sums[j - a] is None:
            continue
        sums[j] = sums[j - a] + [i]

minus = set(sums[-1])
for i, a in enumerate(numbers):
    if i > 0:
        print('-' if i in minus else '+', end='')
    print(a, end='')
print()
