# Списки и изменяемые объекты
a = [1, 2]
b = a
c = a.copy()
b.append(3)
assert a == [1, 2, 3]
assert c == [1, 2]
clean = [x for x in [3, -1, -2, 5] if x >= 0]
assert clean == [3, 5]
