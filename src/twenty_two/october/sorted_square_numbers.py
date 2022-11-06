"""
21st october

Given a list of sorted numbers (can be both negative or positive),
return the list of numbers squared in sorted order.

Solve this problem in O(n) time.
"""


def square_numbers(nums: list) -> list:
    return sorted([num**2 for num in nums])
