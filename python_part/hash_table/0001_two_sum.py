# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit


"""
Hash Table
0001    Two Sum
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @timeit
    def run(self, nums: List[int], target: int) -> List[int]:
        """
        for i in range(0, len(nums)-1):
            tmp = target - nums[i]
            # nums.remove(nums[i])  # FIXME: just record the mistake I made
            new_nums = nums[:i] + nums[i+1:]
            self.logger.info("new_nums: {}".format(new_nums))
            new_set = set(new_nums)
            if tmp in new_set:
                return [i, nums.index(tmp)]
        --
        Wrong Answer

        Input:[3,3], 6
        Output:[0,0]
        Expected:[0,1]
        """

        """
        description
        --
        
        You can return the answer in any order.
        -> think about dict() or set()
        --
        
        result:
        Runtime: 40 ms, faster than 95.52% of Python3 online submissions for Two Sum.
        Memory Usage: 15.4 MB, less than 7.40% of Python3 online submissions for Two Sum.
        """
        lookup = {}
        for idx, num in enumerate(nums):
            if target - num in lookup:
                self.logger.info('lookup: {}'.format(lookup))
                # return [idx, lookup[num]]  # FIXME: just record the mistake I made
                return [lookup[target - num], idx]
            lookup[num] = idx


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(nums=[2, 7, 11, 15], target=9))
    print(sol.run(nums=[3, 2, 4], target=6))
    print(sol.run(nums=[3, 3], target=6))
