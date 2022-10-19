"""
Testing file for problems from october 2022
"""

from src.twenty_two.october.maximum_in_a_stack import MaxStack
from src.twenty_two.october.kth_largest_in_a_list import find_kth_largest


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
