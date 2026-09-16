# Среда Python и числовые выражения
a, b = -7, 3
q, r = a // b, a % b
print(q, r)
assert a == q * b + r
assert 2 + 3 * 4 == 14
