# Сортировки выбором и вставками
def insertion_sort(values):
    a = list(values)
    for i in range(1, len(a)):
        x, j = a[i], i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a

assert insertion_sort([3, 1, 2, 1]) == [1, 1, 2, 3]
