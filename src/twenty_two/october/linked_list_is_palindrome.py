"""
19th october
---
You are given a doubly linked list. Determine if it is a palindrome.

Can you do this for a singly linked list?
"""


class Node(object):
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None


def is_palindrome(node: Node) -> bool:
    right = []
    reverse = []
    prev_node = None
    while node:
        right.append(node.val)
        prev_node = node
        node = node.next
    # do not use list.reverse() built-in function as
    # it has a prev variable and they want you to use it
    while prev_node:
        reverse.append(prev_node.val)
        prev_node = prev_node.prev

    return "".join(right) == "".join(reverse)
