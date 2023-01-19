from typing import List
from collections import Counter, defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        according to instructions: in-place replacement for nums: List[int]
        -> python list operation

        ---
        since it's in-place replacement, we do not take only one action at a time, e.g. only del
        instead, we re-assign the elements "by index"
        note. in python list operation, `remove` by value; both `del` and `pop` by index, however, they are single actions,
        so we keep an eye on indexes, in order to do in-place replacement operations

        idx 0   1  2  3  4  5  6  7  8  9      0  1  2  3  4
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> [0, 1, 2, 3, 4]
        """
        if not nums:
            return 0
        # since this in-place replacement thing, the "targets-to-record" are "indexes"
        position_idx = 0  # this variable records the index whether we should keep the original value, or to replace it into a new element
        for i in range(0, len(nums)):
            if nums[i] == nums[position_idx]:
                pass
            else:
                position_idx += 1
                nums[position_idx] = nums[i]
        return position_idx+1  # for the length, cuz it counts from index 0


# # FIXME: wrong answer
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         """
#         instructions: in-place replacement for nums: List[int]
#         -> python list operation
#
#         ---
#         since it's in-place replacement, we do not take only one action at a time, e.g. only del
#         instead, we re-assign the elements "by index"
#         note. in python list operation, `remove` by value; both `del` and `pop` by index, however, they are single actions,
#         so we keep an eye on indexes, in order to do in-place replacement operations
#
#         idx 0   1  2  3  4  5  6  7  8  9      0  1  2  3  4
#             [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> [0, 1, 2, 3, 4]
#         """
#         # since this in-place replacement thing, it's all about indexes, thus, we need to record it
#         position_idx = 0
#         for i in range(1, len(nums)):
#             if nums[i] == nums[position_idx]:
#                 position_idx += 1
#             else:
#                 nums[position_idx] = nums[i]
#         return position_idx+1
#
#
# """ wrong answer, and according to instructions, we should do in-place replacement
# nums = [0,0,1,1,1,2,2,3,3,4]
#
# Output
# [0,1,1,2,3,4]
# Expected
# [0,1,2,3,4]
# """


# # FIXME: wrong answer
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         contain_lst = list()
#         not_contain_lst = list()
#         check_set = set()
#
#         for num in nums:
#             if num not in check_set:
#                 contain_lst.append(num)
#             else:
#                 not_contain_lst.append(None)
#             check_set.add(num)
#         return len(contain_lst)
#
#
# """ wrong answer, and according to instructions, we should do in-place replacement
# nums = [0,0,1,1,1,2,2,3,3,4]
#
# Output
# [0,0,1,1,1]
# Expected
# [0,1,2,3,4]
# """
#
# print(Solution.removeDuplicates(None, nums=[1, 1, 2]))


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
