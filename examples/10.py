# Кортежи и словари
counts = {}
for word in ["кот", "дом", "кот"]:
    counts[word] = counts.get(word, 0) + 1
assert counts == {"кот": 2, "дом": 1}
assert sorted(counts) == ["дом", "кот"]
