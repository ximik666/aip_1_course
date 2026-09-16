# Линейный и бинарный поиск
def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

assert lower_bound([1, 3, 3, 7], 3) == 1
assert lower_bound([], 3) == 0
