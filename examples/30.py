# Динамическое программирование
def stair_ways(n):
    if type(n) is not int or n < 0:
        raise ValueError("нужно целое n >= 0")
    ways = [1] * (n + 1)
    for i in range(2, n + 1):
        ways[i] = ways[i-1] + ways[i-2]
    return ways[n]

assert stair_ways(0) == 1
assert stair_ways(5) == 8
