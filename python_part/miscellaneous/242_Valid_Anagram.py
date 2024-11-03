# -*- coding: utf-8 -*-
from collections import defaultdict


"""
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dd_1 = defaultdict(int)
        for x in s:
            dd_1[x] += 1
        dd_2 = defaultdict(int)
        for x in t:
            dd_2[x] += 1
        return dd_1 == dd_2


"""
Runtime 11 ms Beats 75.92%
Memory 16.66 MB Beats 94.09%
"""
