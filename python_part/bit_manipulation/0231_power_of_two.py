# -*- coding: utf-8 -*-
from utility.utils import Logger, timeit


"""
Bit Manipulation
0231	Power of Two
https://leetcode.com/problems/power-of-two/
"""

# Time:  O(1)
# Space: O(1)


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @timeit
    def run(self, n: int) -> bool:
        """
        description
        --
        return true if it is a power of two

        Constraints:
        -2^31 <= n <= 2^31 - 1
        --

        Follow up: Could you solve it without loops/recursion?
        """
        # import math
        # return math.log(n, 2).is_integer()
        # FIXME: mistake - 29.000000000000004, might be overflow. So it is better to use multiplication(exponential) rather than division(log)

        """
        the method below
        Runtime: 44 ms, faster than 5.74% of Python3 online submissions for Power of Two.
        Memory Usage: 14.1 MB, less than 66.93% of Python3 online submissions for Power of Two.
        """
        res = list()
        for i in range(0, 35):
            res.append(2 ** i)
        return (n > 0) and (n in res)

    @timeit
    def run_2(self, n: int) -> bool:
        """
        reference
        https://killer0001.blogspot.com/2018/10/python-tips-and-or.html

        - 如果 a 和 b 都是邏輯值, 則 and 和 & ; or 和 | 沒有差異.

        - 如果 a 和 b 是數值變數, 則 & 和 | 為(二進)位運算. 從下例可知:
        &運算 時, 二進制第一碼會取1 (True), 第二碼會取1 (True), 第三碼會取0 (False). 故a & b 會得到6.
        | 運算 時, 二進制第一碼會取1 (True), 第二碼會取1 (True), 第三碼會取1 (True). 故a & b 會得到7.
        --

        example
        n = 4,   4 的二進位 = 100
        n-1 = 3, 3 的二進位 = 011
        -> see the above binary codes as a matrix, we check it column-wise
        -> 4 & 3 -> 4 and 3 -> binary matrix column-wise -> result of binary code = 000 -> equals 0 -> 4 & 3 = 0

        6 & 7 -> binary codes
        110 and
        111
        -> binary matrix column-wise -> result of binary code = 110 -> equals 6 -> 6 & 7 = 6

        10 & 13 -> binary codes
        1010 and
        1101
        -> binary matrix column-wise -> result of binary code = 1000 -> equals 8 -> 10 & 13 = 8
        """
        return (n > 0) and (n & (n-1) == 0)  # FIXME: mistake: (1)need to check n>0 (2)& operation usage (3)this concept to determine the exponential is totally new for me


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(n=1))
    print(sol.run(n=16))
    print(sol.run(n=3))
    print(sol.run(n=4))
    print(sol.run(n=5))
    print('--')
    print(sol.run_2(n=1))
    print(sol.run_2(n=16))
    print(sol.run_2(n=3))
    print(sol.run_2(n=4))
    print(sol.run_2(n=5))
