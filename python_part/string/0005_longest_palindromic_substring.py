# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit

"""
String
0005	Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""


# Time:
# Space:


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    # @timeit
    # def run(self, s: str) -> str:
    #     """
    #
    #     """
    #     # if len(s) == 1:
    #     #     return s
    #     # elif len(s) == 2:
    #     #     return s[0]
    #     # else:
    #     #     from collections import Counter
    #     #     multi_elements = [x for x, cnt in Counter(s).items() if cnt >= 2]
    #     #     for i in range(0, len(s)):

    @timeit
    def run_2(self, s: str) -> str:
        """
        reference
        題解1 - 窮舉搜索(brute force)
        https://algorithm.yuanbin.me/zh-tw/string/longest_palindromic_substring.html

        複雜度分析
        窮舉所有的子串，O(C_n^2) = O(n^2), 每次判斷字符串是否為回文，複雜度為 O(n), 
        故總的時間複雜度為 O(n^3)
        故大數據集下可能 TLE. 使用了 substr 作為臨時子串，
        空間複雜度為 O(n)
        --
        
        Time Limit Exceeded
        Details 
        Last executed input "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
        """  # FIXME: time complexity of this method is O(n^3), it shouldn't be accepted as an answer
        if not s:
            return ''
        n = len(s)
        longest, left, right = 0, 0, 0
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                if self.is_palindrome(substr) and len(substr) > longest:
                    longest = len(substr)
                    left, right = i, j
        # construct longest substr
        result = s[left:right]
        return result

    def is_palindrome(self, s):
        self.logger.info('')
        if not s:
            return False
        # reverse compare
        return s == s[::-1]

    """
    please refer to this:
    https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/longest-palindromic-substring.py
    """


if __name__ == '__main__':
    sol = Solution()
    print(sol.run_2(s="babad"))
    print(sol.run_2(s="cbbd"))
    print(sol.run_2(s="dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"))
