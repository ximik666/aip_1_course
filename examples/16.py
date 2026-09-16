# Комплексные числа и защита первого проекта
def multiply(a, b, c, d):
    return [a*c - b*d, a*d + b*c]

assert multiply(1, 2, 3, 4) == [-5, 10]
assert multiply(0, 0, 3, 4) == [0, 0]
