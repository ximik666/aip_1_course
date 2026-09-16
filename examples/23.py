# Очередь и моделирование обслуживания
from collections import deque
q = deque()
q.append("A")
q.append("B")
assert q.popleft() == "A"
q.append("C")
assert list(q) == ["B", "C"]
