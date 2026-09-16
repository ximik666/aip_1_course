# Переменные и ввод данных
price_cents = 1250
count = 3
total = price_cents * count
print(f"{total // 100}.{total % 100:02d}")
assert total == 3750
