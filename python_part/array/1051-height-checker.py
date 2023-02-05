from typing import *
from collections import defaultdict


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Runtime 34 ms Beats 87.38% Memory 13.8 MB Beats 94.44%
        """
        sort_heights = sorted(heights)
        return sum([0 if heights[i] == sort_heights[i] else 1 for i in range(len(heights))])


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Runtime 36 ms Beats 78.46% Memory 13.9 MB Beats 8.44%
        """
        od_heights = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if heights[i] != od_heights[i]:
                ans += 1
        return ans