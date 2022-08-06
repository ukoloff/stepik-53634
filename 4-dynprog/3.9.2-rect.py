f = open('rectangle.in')


def readi():
    return [int(z) for z in f.readline().split()]


n, m = readi()
numbers = [readi() for i in range(n)]
(q,) = readi()
qs = [readi() for i in range(q)]

cumsum = [[0] * (1+len(numbers[0])) for i in range(-1, len(numbers))]

for i in range(1, len(cumsum)):
    for j in range(1, len(cumsum[0])):
        cumsum[i][j] = numbers[i - 1][j - 1] + \
            cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1]

answers = []
for x1, x2, y1, y2 in qs:
    answer = cumsum[x2][y2] - cumsum[x1-1][y2] - cumsum[x2][y1-1] + cumsum[x1-1][y1-1]
    answers.append(answer)

print(*answers)
print(sum(answers))
