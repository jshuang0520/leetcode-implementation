# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit


"""
Hash Table
0003	Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

# Time:  O(n)
# Space: O(1)


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @timeit
    def run(self, s: str) -> int:
        """
        Given a string s,
        find the length of the longest substring without repeating characters.

        -> 'without repeating' -> think about dict() or set()
        """
        lookup = dict()
        left_idx, result = 0, 0
        for i in range(0, len(s)):
            if s[i] in lookup:
                # left_idx = max(left_idx, lookup[s[i]])  # FIXME: just record the mistake I made
                left_idx = max(left_idx, lookup[s[i]] + 1)
            lookup[s[i]] = i
            result = max(result, i - left_idx + 1)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(s="abcabcbb"))
    print(sol.run(s="bbbbb"))
    print(sol.run(s="pwwkew"))
    print(sol.run(s=""))
