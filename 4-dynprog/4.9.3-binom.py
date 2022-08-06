def binom(n, k):
    z = [0] * k
    z.append(1)
    for i in range(n):
        for j, v in enumerate(z):
            if j > 0:
                z[j - 1] += v
    return z[0]


print(binom(3, 2))
print(binom(50, 20))
