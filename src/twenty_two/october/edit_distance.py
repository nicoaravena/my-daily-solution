"""
15th october
---
Given two strings, determine the edit distance between them.
The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution)
needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2
(substitute b for s, and insert a t).
"""

import difflib


def distance(s1: str, s2: str):
    # Fill this in.
    d = difflib.SequenceMatcher(lambda x: x == " ", s1, s2)
    length = max(len(s1), len(s2))

    for match in d.get_matching_blocks():
        length -= match.size
    return length
