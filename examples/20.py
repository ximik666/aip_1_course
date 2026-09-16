# Слияние и сортировка подсчётом
def counting_sort(a, k):
    counts = [0] * (k + 1)
    for x in a:
        if type(x) is not int or not 0 <= x <= k:
            raise ValueError("вне диапазона")
        counts[x] += 1
    return [x for x in range(k + 1) for _ in range(counts[x])]

assert counting_sort([3, 0, 3, 1], 3) == [0, 1, 3, 3]
