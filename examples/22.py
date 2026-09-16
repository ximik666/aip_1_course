# Стек и проверка скобок
def balanced(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for c in text:
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack

assert balanced("a*(b+[c])")
assert not balanced("([)]")
