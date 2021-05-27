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
        for i in range(0, len(nums)-1):
            tmp = target - nums[i]
            # nums.remove(nums[i])
            new_nums = nums[:i] + nums[i+1 :]
            self.logger.info("new_nums: {}".format(new_nums))
            new_set = set(new_nums)
            if tmp in new_set:
                return [i, nums.index(tmp)]
            else:
                pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(nums=[2, 7, 11, 15], target=9))
    print(sol.run(nums=[3, 2, 4], target=6))
    print(sol.run(nums=[3, 3], target=6))
