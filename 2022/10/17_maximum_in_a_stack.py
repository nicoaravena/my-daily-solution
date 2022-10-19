"""
Implement a class for a stack that supports all the regular functions (push, pop)
and an additional function of max() which returns the maximum element in the stack
(return None if the stack is empty).

Each method should run in constant time.
"""

# deque has a faster performance in some cases than lists
from collections import deque


class MaxStack:
    def __init__(self):
        self.stack = deque()

    def push(self, val: int):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def max(self):
        return max(self.stack)


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
