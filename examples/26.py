# Метод Гаусса и ранг
A = [[0.0, 2.0], [3.0, 4.0]]
A[0], A[1] = A[1], A[0]
sign = -1
determinant = sign * A[0][0] * A[1][1]
assert determinant == -6.0
