# Матрицы и операции над таблицами
A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 0], [0, 1], [1, 1]]
C = [[sum(A[i][k] * B[k][j] for k in range(3))
      for j in range(2)] for i in range(2)]
assert C == [[4, 5], [10, 11]]
T = [list(col) for col in zip(*A)]
assert T == [[1, 4], [2, 5], [3, 6]]
