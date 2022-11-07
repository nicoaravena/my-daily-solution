"""
23th october

Find all words that are concatenations of a list.

Input:
["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]

Output:
['techlead', 'catsdog']
"""

import itertools


class Solution(object):
    def find_all_concatenated_words_in_a_dict(self, words):
        """
        If the concatenated words will never be formed by the same word (e.g: techtech)
        then it is better to use itertools.permutations(words, 2) to reduce length
        """
        concatenated_words = [
            "".join(item)
            for item in itertools.product(words, words)
            if "".join(item) in words
        ]

        return concatenated_words
