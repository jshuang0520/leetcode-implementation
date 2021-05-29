# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit


"""
Array
0189	Rotate Array
https://leetcode.com/problems/rotate-array/
"""


# Time:  O(n)
# Space: O(1)


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    # @staticmethod
    # def rotate(num_list: List[int]) -> List[int]:
    #     """
    #     rotate the last element to become the first one
    #     """
    #     element = num_list.pop(-1)
    #     num_list.insert(0, element)
    #     return num_list
    #
    # @timeit
    # def run(self, nums: List[int], k: int) -> None:
    #     """
    #     description
    #     Given an array
    #     -> Array
    #     """
    #     for i in range(0, k):
    #         nums = self.rotate(num_list=nums)
    #     self.logger.info('nums: {}'.format(nums))

    @timeit
    def run(self, nums: List[int], k: int) -> None:
        """
        description
        Given an array
        -> Array
        --

        Runtime: 3072 ms, faster than 11.56% of Python3 online submissions for Rotate Array.
        Memory Usage: 25.3 MB, less than 81.99% of Python3 online submissions for Rotate Array.
        """
        for i in range(0, k):
            element = nums.pop(-1)
            nums.insert(0, element)
        self.logger.info('nums: {}'.format(nums))

    @timeit
    def run_2(self, nums: List[int], k: int) -> None:
        """
        description
        Given an array
        -> Array
        --

        Runtime Error
        IndexError: list index out of range
        Last executed input
        nums=[-1], k=2
        """
        # tmp = list()
        # for i in range(0, k):
        #     tmp.append(nums[-1])
        #     del nums[-1]
        # tmp = tmp[::-1]
        # # nums = tmp + nums  # it didn't modify the nums list directly, so it's an unacceptable answer
        # nums[:] = tmp + nums  # FIXME: mistake - "nums[:] = ..." -> we assign the list this way to modify the nums list directly
        # self.logger.info('nums: {}'.format(nums))

    @timeit
    def run_3(self, nums: List[int], k: int) -> None:
        """
        description
        Given an array
        -> Array
        --
        
        Wrong Answer
        Details 
        Input nums=[1,2], k=3
        Output [1,2]
        Expected [2,1]
        """  # FIXME: mistake - we need to consider the length of nums and k
        # nums[:] = nums[-k::] + nums[:-k:]  # FIXME: mistake - "nums[:] = ..." -> we assign the list this way to modify the nums list directly
        # self.logger.info('nums: {}'.format(nums))


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
    print(sol.run(nums=[-1, -100, 3, 99], k=2))
