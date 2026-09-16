# Цикл while и завершение
n = 507
total = 0
while n > 0:
    total += n % 10
    n //= 10
assert total == 12
