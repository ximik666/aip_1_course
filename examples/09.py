# Функции и контракты
def mean(values):
    """Среднее или None для пустой последовательности."""
    if not values:
        return None
    return sum(values) / len(values)

assert mean([2, 4]) == 3
assert mean([]) is None
