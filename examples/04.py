# Логика и ветвления
score = 70
if not 0 <= score <= 100:
    result = "error"
elif score >= 85:
    result = "5"
elif score >= 70:
    result = "4"
elif score >= 60:
    result = "3"
else:
    result = "2"
assert result == "4"
