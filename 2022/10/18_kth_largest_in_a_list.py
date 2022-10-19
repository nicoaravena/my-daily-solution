"""
Given a list, find the k-th largest element in the list.

Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
"""


def find_kth_largest(nums: list, k: int) -> int:
    highest = -1
    while k > 0:
        k -= 1
        highest = max(nums)
        nums.remove(highest)
    return highest


print(find_kth_largest([3, 5, 2, 4, 6, 8], 3))
# 5
