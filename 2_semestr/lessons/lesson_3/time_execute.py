from collections import deque
import random
import time
from tracemalloc import start
numbers = []
for x in range(1000000):
    numbers.append(random.randint(0,100000))

for k in range(100000):
    start_time = time.perf_counter()
    last_item = numbers.pop()
print(time.perf_counter()-start_time)

for k in range(100000):
    start_time = time.perf_counter()
    first_item = numbers.pop(0)

print(time.perf_counter()-start_time)


numbers = deque()
# Use append like before to add elements
for x in range(1000000):
    numbers.append(random.randint(0,100000))

# You can pop like a stack
for k in range(100000):
    start_time = time.perf_counter()
    last_item = numbers.pop()
print(time.perf_counter()-start_time)

# You can dequeue like a queue
for k in range(100000):
    start_time = time.perf_counter()
    first_item = numbers.popleft()

print(time.perf_counter()-start_time)
