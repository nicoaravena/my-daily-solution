"""
Testing file for problems from october 2022
"""

from src.twenty_two.october.edit_distance import distance
from src.twenty_two.october.rotate_matrix import rotate
from src.twenty_two.october.maximum_in_a_stack import MaxStack
from src.twenty_two.october.kth_largest_in_a_list import find_kth_largest
from src.twenty_two.october.linked_list_is_palindrome import Node, is_palindrome


def test_distance():
    assert distance('biting', 'sitting') == 2
    assert distance('billing', 'sitting') == 3
    assert distance('silling', 'sitting') == 2
    assert distance('asdf', 'qwer') == 4


def test_rotate():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotated_mat = rotate(mat)
    result = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotated_mat == result


def test_find_kth_largest():
    assert find_kth_largest([3, 5, 2, 4, 6, 8], 3) == 5


def test_max_stack():
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    assert s.max() == 3
    s.pop()
    s.pop()
    assert s.max() == 2


def test_is_palindrome():
    node = Node("a")
    node.next = Node("b")
    node.next.prev = node
    node.next.next = Node("b")
    node.next.next.prev = node.next
    node.next.next.next = Node("a")
    node.next.next.next.prev = node.next.next

    assert is_palindrome(node)


def test_is_not_palindrome():
    node = Node("a")
    node.next = Node("b")
    node.next.prev = node
    node.next.next = Node("c")
    node.next.next.prev = node.next
    node.next.next.next = Node("a")
    node.next.next.next.prev = node.next.next

    assert not is_palindrome(node)
