from collections import deque

stack = deque()

stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack)

print(stack[-1])

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)