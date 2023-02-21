# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        strategy: result times 10, and then add ones digit

        --
        Runtime 34 ms Beats 67.73% Memory 13.9 MB Beats 49.55%
        """
        total = 0
        # lst = list()

        for digit in digits:
            total = total * 10 + digit
        total += 1
        # str_total = str(total)
        # for elem in str_total:
        #     lst.append(int(elem))
        return list(map(int, str(total)))


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        strategy: string concat -> to integer -> plus one -> back to list form

        --
        Runtime 38 ms Beats 41.20% Memory 13.9 MB Beats 49.55%
        """
        lst = list()
        if digits:
            # integer = str(int(''.join(str(x) for x in digits)) + 1)
            integer = str(int(''.join(str(x) for x in digits)) + 1)
            for x in integer:
                lst.append(int(x))
        return lst


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # """
        # Runtime 41 ms Beats 33.4% Memory 13.9 MB Beats 8.48%
        # """
        # string = ''
        # for s in digits:
        #     string += str(s)
        # string = str(int(string) + 1)
        # return list(map(int, string))

        """
        Runtime 32 ms Beats 81.3% Memory 14.2 MB Beats 8.48%
        """
        res = int(''.join(str(x) for x in digits))
        res += 1
        return list(map(int, str(res)))


"""
Array
0066	Plus One
https://leetcode.com/problems/plus-one/
"""


# Time:  O(n)
# Space: O(1)


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @timeit
    def run(self, digits: List[int]) -> List[int]:
        """
        description
        Given a non-empty array
        -> Array
        --

        Constraints:
        1 <= digits.length <= 100
        0 <= digits[i] <= 9
        """

        """
        Wrong Answer
        --
        Details 
        Input [9]
        Output [10]
        Expected [1,0] -> due to constraint 0 <= digits[i] <= 9
        """
        # digits[-1] += 1
        # return digits  # FIXME: mistake - if input [9], output [1, 0]

        """
        Wrong Answer
        --
        Details 
        Input [9, 9]
        Output [9, 1, 0]
        Expected [1, 0, 0]
        -> Input: digits = [1,2,3], Output: [1,2,4], Explanation: The array represents the integer 123.
        And 123 + 1 = 124 -> output [1, 2, 4]
        """  # FIXME: mistake - if input [9, 9], the output is NOT [9, 10] -> [9, 1, 0], but [9, 9] represents 99, 99 + 1 = 100 -> output [1, 0, 0]
        # digits[-1] += 1
        # # res = list()
        # # for i in range(0, len(digits)):
        # #     if len(str(digits[i])) > 1:
        # #         digits.insert(i, [int(x) for x in str(digits[i])])
        # if digits[-1] == 10:
        #     digits[-1] = 1
        #     digits.append(0)
        # return digits

        """
        last try, after figuring out the meaning of this topic finally
        --
        Runtime: 32 ms, faster than 63.10% of Python3 online submissions for Plus One.
        Memory Usage: 14.2 MB, less than 73.03% of Python3 online submissions for Plus One.
        """
        res = int(''.join(str(x) for x in digits))
        res += 1
        return list(map(int, str(res)))
        # for i in range(0, len(str(res))):


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(digits=[1, 2, 3]))
    print(sol.run(digits=[4, 3, 2, 1]))
    print(sol.run(digits=[9]))
    print(sol.run(digits=[9, 9]))
