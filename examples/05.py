# Цикл for и накопление
total = 0
count = 0
for x in [3, -2, 0, 7]:
    if x >= 0:
        total += x
        count += 1
assert (total, count) == (10, 3)
