"""
20th October
---
Given 2 binary trees t and s, find if s has an equal subtree in t,
where the structure and the values are the same. Return True if it exists,
otherwise return False.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def find_subtree(s: Node, t: Node) -> bool:
    if repr(s) == repr(t):
        return True
    else:
        if isinstance(t.left, Node) and isinstance(t.right, Node):
            return find_subtree(s, t.left) or find_subtree(s, t.right)
        elif isinstance(t.left, Node):
            return find_subtree(s, t.left)
        elif isinstance(t.right, Node):
            return find_subtree(s, t.right)

    return False
