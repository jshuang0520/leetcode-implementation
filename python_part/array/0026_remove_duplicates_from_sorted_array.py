# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit

"""
Array
0026	Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


# Time:  O(n)
# Space: O(1)


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @timeit
    def run(self, nums: List[int]) -> int:
        """
        description
        --
        Do not allocate extra space for another array, you must do this
        by modifying the input array in-place with O(1) extra memory.
        """
        if not nums:  # FIXME: mistake: need to consider the 'not' condition first
            return 0

        previous_idx = 0  # FIXME: mistake: need this variable
        for i in range(1, len(nums)):  # FIXME: mistake: should be 1, not 0
            if nums[previous_idx] == nums[i]:
                pass
            else:
                previous_idx += 1  # FIXME: mistake: need to put this row prior to the row below
                nums[previous_idx] = nums[i]  # FIXME: mistake: need to assign the previous index of element to the non-duplicate one

        self.logger.info('nums: {}'.format(nums))

        # return len(nums)  # FIXME: mistake
        return previous_idx + 1  # , nums[:previous_idx + 1]

    @timeit
    def run_2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        last = 0
        for i in range(len(nums)):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]

        self.logger.info('nums: {}'.format(nums))

        return last + 1  # , nums[:last + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(nums=[1, 1, 2]))
    print(sol.run(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print('--')
    print(sol.run_2(nums=[1, 1, 2]))
    print(sol.run_2(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
