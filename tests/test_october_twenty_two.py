"""
Testing file for problems from october 2022
"""

from src.twenty_two.october import edit_distance
from src.twenty_two.october import find_subtree
from src.twenty_two.october import rotate_matrix
from src.twenty_two.october import maximum_in_a_stack
from src.twenty_two.october import kth_largest_in_a_list
from src.twenty_two.october import linked_list_is_palindrome
from src.twenty_two.october import sorted_square_numbers


def test_distance():
    assert edit_distance.distance('biting', 'sitting') == 2
    assert edit_distance.distance('billing', 'sitting') == 3
    assert edit_distance.distance('silling', 'sitting') == 2
    assert edit_distance.distance('asdf', 'qwer') == 4


def test_rotate():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotated_mat = rotate_matrix.rotate(mat)
    result = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotated_mat == result


def test_find_kth_largest():
    assert kth_largest_in_a_list.find_kth_largest([3, 5, 2, 4, 6, 8], 3) == 5


def test_max_stack():
    s = maximum_in_a_stack.MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    assert s.max() == 3
    s.pop()
    s.pop()
    assert s.max() == 2


def test_is_palindrome():
    node = linked_list_is_palindrome.Node("a")
    node.next = linked_list_is_palindrome.Node("b")
    node.next.prev = node
    node.next.next = linked_list_is_palindrome.Node("b")
    node.next.next.prev = node.next
    node.next.next.next = linked_list_is_palindrome.Node("a")
    node.next.next.next.prev = node.next.next

    assert linked_list_is_palindrome.is_palindrome(node)


def test_is_not_palindrome():
    node = linked_list_is_palindrome.Node("a")
    node.next = linked_list_is_palindrome.Node("b")
    node.next.prev = node
    node.next.next = linked_list_is_palindrome.Node("c")
    node.next.next.prev = node.next
    node.next.next.next = linked_list_is_palindrome.Node("a")
    node.next.next.next.prev = node.next.next

    assert not linked_list_is_palindrome.is_palindrome(node)


def test_find_subtree_true_on_left():
    t3 = find_subtree.Node(4, find_subtree.Node(3), find_subtree.Node(2))
    t2 = find_subtree.Node(5, find_subtree.Node(4), find_subtree.Node(-1))
    t = find_subtree.Node(1, t3, t2)

    s = find_subtree.Node(4, find_subtree.Node(3), find_subtree.Node(2))
    assert find_subtree.find_subtree(s, t)


def test_find_subtree_true_on_right():
    t3 = find_subtree.Node(4, find_subtree.Node(3), find_subtree.Node(2))
    t2 = find_subtree.Node(5, find_subtree.Node(4), find_subtree.Node(-1))
    t = find_subtree.Node(1, t2, t3)

    s = find_subtree.Node(4, find_subtree.Node(3), find_subtree.Node(2))
    assert find_subtree.find_subtree(s, t)


def test_find_subtree_true_on_left_with_right_none():
    t2 = find_subtree.Node(4, find_subtree.Node(3), find_subtree.Node(2))
    t = find_subtree.Node(1, t2, None)

    s = find_subtree.Node(4, find_subtree.Node(3), find_subtree.Node(2))
    assert find_subtree.find_subtree(s, t)


def test_find_subtree_true_on_right_wih_left_none():
    t2 = find_subtree.Node(4, find_subtree.Node(3), find_subtree.Node(2))
    t = find_subtree.Node(1, None, t2)

    s = find_subtree.Node(4, find_subtree.Node(3), find_subtree.Node(2))
    assert find_subtree.find_subtree(s, t)


def test_sorted_square_numbers():
    result = sorted_square_numbers.square_numbers([-5, -3, -2, -1, 0, 1, 4, 5])
    assert isinstance(result, list)
    assert result == [0, 1, 1, 4, 9, 16, 25, 25]
    result = sorted_square_numbers.square_numbers([-5, -3, -1, 0, 1, 4, 5])
    assert isinstance(result, list)
    assert result == [0, 1, 1, 9, 16, 25, 25]
