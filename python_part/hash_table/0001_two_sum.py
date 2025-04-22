# -*- coding: utf-8 -*-
"""
Hash Table
0001    Two Sum
https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()  # key: num, val: its idx
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            seen[nums[i]] = i
        return [-1, -1]
    

# -------------------------------------------------------------------------------------------------

from collections import defaultdict
from typing import List
# from utility.utils import Logger, timeit

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """improve the previous idea with a decent time complexity
        Runtime 0 ms Beats 100.00%
        Memory 17.81 MB Beats 22.16%
        """
        pool = dict()
        for idx, num in enumerate(nums):
            target_elem = target - num
            if target_elem in pool:
                return [idx, pool[target_elem]]
            pool[num] = idx  # brilliant mechanism to prevent from adding the current idx! You first search for the pools, and then add the new information after the if conditional statement


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """very slow implementation!
        Runtime 963 ms Beats 31.28%
        Memory 17.23 MB Beats 91.79%
        """
        for idx, num in enumerate(nums):
            target_elem = target - num
            for i in range(idx + 1, len(nums)):
                if nums[i] == target_elem:
                    return [idx, i]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        to record metadata for quick retrieval -> defaultdict
        calculation relates to index
        """
        dd = defaultdict(list)
        # ans_lst = list()

        # (num + ans = target) => (ans = target - num)
        for idx, num in enumerate(nums):
            dd[num].append(idx)
        # print(f'finished dd: {dd}')

        keys_set = set(dd.keys())
        for key, value in dd.items():
            # print(f'key, value: {key, value}')
            # print(f'dd[key]: {dd[key]}')
            # print(f'dd[target - key]: {dd[target - key]}')
            if target == 2*key:
                if len(value) == 2:
                    return value
            else:
                if value and ((target - key) in keys_set):  # FIXME: RuntimeError: dictionary changed size during iteration -> in python defaultdict, if a key was not existed, it will create one instantly -> so in this for loop to check .items(), it will encounter RuntimeError: dictionary changed size during iteration
                    # ans_lst.__iadd__(value)
                    # ans_lst.__iadd__(dd[target - key])
                    return value.__iadd__(dd[target - key])  # __iadd__ means in-place-add


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         """
#         to record metadata for quick retrieval -> defaultdict
#         calculation relates to index
#         """
#         dd = defaultdict(list)
#         ans_lst = list()
#
#         # (num + ans = target) => (ans = target - num)
#         for idx, num in enumerate(nums):
#             dd[num].append(idx)
#         print(f'finished dd: {dd}')
#
#         for key, value in dd.items():
#             print(f'key, value: {key, value}')
#             print(f'dd[key]: {dd[key]}')
#             print(f'dd[target - key]: {dd[target - key]}')
#             if target == 2*key:
#                 if len(value) == 2:
#                     return value
#             else:
#                 if value and (dd[target - key]):  # FIXME: RuntimeError: dictionary changed size during iteration -> in python defaultdict, if a key was not existed, it will create one instantly -> so in this for loop to check .items(), it will encounter RuntimeError: dictionary changed size during iteration
#                     ans_lst.__iadd__(value)
#                     ans_lst.__iadd__(dd[target - key])
#                     return ans_lst  # __iadd__ means in-place-add
# print(Solution.twoSum(None, nums=[3,2,4], target=6))
# print('----------------------------------------------------')
# print(Solution.twoSum(None, nums=[2,5,5,11], target=10))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        "array" of int + "add up to target"
        -> to find "something to match"
        -> "Now, I have a half one, if the other correspondence shows up, then I can know!"
        -> to store these to-be-used information into a data structure that data can be retrieved quickly in the future
        -> collect "key" to a defaultdict
        """
        dd = defaultdict(int)
        idx_dict = defaultdict(list)
        for idx, num in enumerate(nums):
            idx_dict[num].append(idx)

            dd[num] += 1
            dd[target-num] += 0
            # print(f'dd: {dd}')
            if target == 2*num:
                if dd[num] == 2:
                    return idx_dict[num]
            elif dd[target-num] == 1:
                return [idx_dict[num][0], idx_dict[target-num][0]]
            else:
                None

        # dd = defaultdict(int)
        # idx_dict = defaultdict(list)
        # for idx, num in enumerate(nums):
        #     idx_dict[num].append(idx)
        #
        #     if num % target == 0:
        #         return idx_dict[num]
        #     else:
        #         dd[num] += 1
        #         dd[target - num] += 0
        #     if dd[target - num] == 1:
        #         return idx_dict[num]


print(Solution.twoSum(None, nums=[3,2,4], target=6))


# ----------------------------------------------------------------------------------------
#
# class Solution:
#     def __init__(self):
#         self.logger = Logger().get_logger('answer')
#
#     @timeit
#     def run(self, nums: List[int], target: int) -> List[int]:
#         """
#         for i in range(0, len(nums)-1):
#             tmp = target - nums[i]
#             # nums.remove(nums[i])  # FIXME: just record the mistake I made
#             new_nums = nums[:i] + nums[i+1:]
#             self.logger.info("new_nums: {}".format(new_nums))
#             new_set = set(new_nums)
#             if tmp in new_set:
#                 return [i, nums.index(tmp)]
#         --
#         Wrong Answer
#
#         Input:[3,3], 6
#         Output:[0,0]
#         Expected:[0,1]
#         """
#
#         """
#         description
#         --
#
#         You can return the answer in any order.
#         -> think about dict() or set()
#         --
#
#         result:
#         Runtime: 40 ms, faster than 95.52% of Python3 online submissions for Two Sum.
#         Memory Usage: 15.4 MB, less than 7.40% of Python3 online submissions for Two Sum.
#         """
#         lookup = {}
#         for idx, num in enumerate(nums):
#             if target - num in lookup:
#                 self.logger.info('lookup: {}'.format(lookup))
#                 # return [idx, lookup[num]]  # FIXME: just record the mistake I made
#                 return [lookup[target - num], idx]
#             lookup[num] = idx
#
#
# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.run(nums=[2, 7, 11, 15], target=9))
#     print(sol.run(nums=[3, 2, 4], target=6))
#     print(sol.run(nums=[3, 3], target=6))
