# Измерение производительности
from random import Random
from time import perf_counter
from statistics import median
rng = Random(42)
base = [rng.randrange(1000) for _ in range(1000)]
times = []
for _ in range(5):
    sample = base.copy()
    start = perf_counter()
    result = sorted(sample)
    times.append(perf_counter() - start)
    assert result == sorted(base)
assert median(times) >= 0
