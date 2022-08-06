f = open('bug2.in')
costs = [[int(z) for z in line.split()]for line in f]


def gather(costs):
    dirs = []
    bests = []
    prev = None
    for i, row in enumerate(costs):
        dir = []
        dirs.append(dir)
        sums = []
        bests.append(sums)
        for j, cell in enumerate(row):
            options = []
            if i > 0:
                options.append([prev[j], 'D'])
            if j > 0:
                options.append([sums[-1], 'R'])
            if len(options) == 0:
                options.append([0, '.'])
            z = max(options)
            sums.append(z[0] + costs[i][j])
            dir.append(z[1])
        prev = sums
    i, j = -1, -1
    path = []
    while True:
        c = dirs[i][j]
        if c == 'R':
            j -= 1
        elif c == 'D':
            i -= 1
        else:
            break
        path.append(c)
    print(bests[-1][-1])
    print(''.join(reversed(path)))


gather(costs)
