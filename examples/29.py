# Итераторы и генераторы
def squares(n):
    for i in range(n):
        yield i * i

g = squares(4)
assert next(g) == 0
assert list(g) == [1, 4, 9]
assert list(g) == []
assert sum(x*x for x in range(4)) == 14
