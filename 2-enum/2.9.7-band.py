def bands(n, m, head=''):
    """
    Расстановка фишек. Имеется полоса размера 1×n,
    разбитая на единичные клетки.
    Нужно расставить в клетках полосы m фишек,
    чтобы никакие две фишки не стояли в соседних клетках.
    Выведите все возможные расстановки.

    Входные данные: Натуральные числа nn и mm.
    """
    if m == 0:
        if n >= 0:
            yield head + '.' * n
        return
    if n < 2 * m - 1:
        return
    if n == 2 * m - 1:
        yield head + ('.*' * m)[1:]
        return
    yield from bands(n - 2, m - 1, head + '*.')
    yield from bands(n - 1, m, head + '.')

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
