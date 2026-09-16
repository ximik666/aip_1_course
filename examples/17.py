# Сложность алгоритмов
n = 5
pairs = 0
for i in range(n):
    for j in range(i + 1, n):
        pairs += 1
assert pairs == n * (n - 1) // 2
