# Исключения и проверка данных
def positive_int(text):
    value = int(text)
    if value <= 0:
        raise ValueError("нужно положительное число")
    return value

assert positive_int("12") == 12
try:
    positive_int("0")
except ValueError:
    pass
else:
    raise AssertionError("ожидали ValueError")
