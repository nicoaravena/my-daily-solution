"""
22nd october

Given two binary trees that are duplicates of one another,
and given a node in one tree, find that corresponding node in the second tree.

For instance, in the tree below, we're looking for Node #4.

For this problem, you can assume that:
- There can be duplicate values in the tree
  (so comparing node1.value == node2.value isn't going to work).

Can you solve this both recursively and iteratively?
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_node(a: Node, b: Node, node: Node) -> Node:
    if not a and not b:
        return None
    if (
        node.val == b.val == a.val
        and isinstance(node.left, Node)
        and isinstance(a.left, Node)
        and isinstance(b.left, Node)
        and node.left.val == a.left.val == b.left.val
        and isinstance(node.right, Node)
        and isinstance(a.right, Node)
        and isinstance(b.right, Node)
        and node.right.val == a.right.val == b.right.val
    ):
        return node.val
    elif (
        node.val == b.val == a.val
        and node.left is None
        and a.left is None
        and b.left is None
        and isinstance(node.right, Node)
        and isinstance(a.right, Node)
        and isinstance(b.right, Node)
        and node.right.val == a.right.val == b.right.val
    ):
        return node.val
    elif (
        node.val == b.val == a.val
        and isinstance(node.left, Node)
        and isinstance(a.left, Node)
        and isinstance(b.left, Node)
        and node.left.val == a.left.val == b.left.val
        and node.right is None
        and a.right is None
        and b.right is None
    ):
        return node.val
    elif (
        node.val == b.val == a.val
        and node.left is None
        and a.left is None
        and b.left is None
        and node.right is None
        and a.right is None
        and b.right is None
    ):
        return node.val
    else:
        return find_node(a.left, b.left, node) or find_node(a.right, b.right, node)
