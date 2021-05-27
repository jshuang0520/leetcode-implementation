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

        --
        result

        Runtime: 24 ms, faster than 95.27% of Python3 online submissions for Number         of 1 Bits.
        Memory Usage: 14.2 MB, less than 36.17% of Python3 online submissions for           Number of 1 Bits.
        """
        # str_n = str(n)  # FIXME: just record the mistake I made
        str_n = str(bin(n))
        self.logger.info('str_n: {}'.format(str_n))
        return str_n.count('1')


if __name__ == '__main__':
    sol = Solution()
    sol.run(n=11111111111111111111111111111101)
