"""
16th october
---
Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.
"""

from collections import deque


def rotate(mat: list):
    # Fill this in.
    new_matrix = [deque() for _ in range(len(mat))]

    for row in mat:
        for idx, col in enumerate(row):
            new_matrix[idx].appendleft(col)

    return [list(item) for item in new_matrix]
