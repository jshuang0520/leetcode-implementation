# according to results below, assign a variable to string, and do the string operation can be faster


class Solution:
    """
    Runtime 27 ms Beats 95.54% Memory 13.9 MB Beats 46.56%
    """
    def hammingWeight(self, n: int) -> int:
        str_n = str(bin(n))
        return str_n.count('1')


class Solution:
    """
    Runtime 36 ms Beats 66.11% Memory 13.8 MB Beats 46.56%
    """
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        return bin_n.count('1')


class Solution:
    """
    Runtime 36 ms Beats 66.11% Memory 13.8 MB Beats 93.78%
    """
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')


class Solution:
    """
    Runtime 32 ms Beats 81.98% Memory 13.9 MB Beats 6.69%
    """
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


# -*- coding: utf-8 -*-
from utility.utils import Logger, timeit


"""
Bit Manipulation
0191    Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
"""


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @timeit
    def run(self, n: int) -> int:
        """
        reference
        google: python count bits 1
        https://www.tutorialspoint.com/number-of-1-bits-in-python

        google: python turn binary string to int stack overflow
        https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int

        --
        result

        Runtime: 24 ms, faster than 95.27% of Python3 online submissions for Number of 1 Bits.
        Memory Usage: 14.2 MB, less than 36.17% of Python3 online submissions for Number of 1 Bits.
        """
        # str_n = str(n)  # FIXME: just record the mistake I made
        str_n = str(bin(n))
        self.logger.info('str_n: {}'.format(str_n))
        return str_n.count('1')


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(n=int('00000000000000000000000000001011', 2)))
    print(sol.run(n=int('00000000000000000000000010000000', 2)))
    print(sol.run(n=int('11111111111111111111111111111101', 2)))
