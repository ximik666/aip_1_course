# Графы и поиск в ширину
from collections import deque
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
distance = {"A": 0}
q = deque(["A"])
while q:
    v = q.popleft()
    for u in graph[v]:
        if u not in distance:
            distance[u] = distance[v] + 1
            q.append(u)
assert distance["D"] == 2
