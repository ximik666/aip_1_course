# Строки и обработка текста
s = "  Анна   ИВАНОВА  "
words = s.casefold().split()
normalized = " ".join(words)
assert normalized == "анна иванова"
assert "level" == "level"[::-1]
