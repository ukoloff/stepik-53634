f = open('time2.in')

todos = [[int(z) for z in f.readline().split()]
         for i in range(int(f.readline()))]

opt = {0: 0}

for t, d in todos:
    for n, finish in [(k+1, v+t) for k, v in opt.items() if v <= d]:
        if n not in opt or finish < opt[n]:
            opt[n] = finish

print(max(opt.keys()))
