# Множества и выбор структуры данных
expected = {"a", "b", "c"}
arrived = {"b", "c", "d"}
assert expected - arrived == {"a"}
assert arrived - expected == {"d"}
assert expected & arrived == {"b", "c"}
