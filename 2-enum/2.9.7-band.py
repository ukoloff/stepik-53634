def bands(n, m):
    """
    Расстановка фишек. Имеется полоса размера 1×n,
    разбитая на единичные клетки.
    Нужно расставить в клетках полосы m фишек,
    чтобы никакие две фишки не стояли в соседних клетках.
    Выведите все возможные расстановки.

    Входные данные: Натуральные числа n и m.
    """
    if m == 0:
        if n >= 0:
            yield '.' * n
        return
    if n < 2 * m - 1:
        return
    if n == 2 * m - 1:
        yield ('.*' * m)[1:]
        return
    yield from ('*.' + tail for tail in bands(n - 2, m - 1))
    yield from ('.' + tail for tail in bands(n - 1, m))

# print(*bands(5, 2), sep='\n')
# z = bands(5, 2)
# for i in range(6):
#   next(z)
# # next(z)
# print(next(z))

from itertools import islice
print(*islice(bands(7, 3), 6, 7))
# print(*bands(7, 3), sep='\n')

print(*islice(bands(25, 8), 24007, 24008))
