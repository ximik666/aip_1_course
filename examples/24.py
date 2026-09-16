# Рекурсия и стек вызовов
def factorial(n):
    if type(n) is not int or n < 0:
        raise ValueError("нужно целое n >= 0")
    if n == 0:
        return 1
    return n * factorial(n - 1)

assert factorial(0) == 1
assert factorial(5) == 120
