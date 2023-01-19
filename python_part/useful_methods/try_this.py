from typing import *


class Solution:
    def remove_duplicates(self, nums: List) -> List:
        """
        since it's a "sorted list"
        we can remove the duplicates by recording indexes
        """
        non_duplicate_lst = list()
        non_duplicate_lst.append(nums[0])

        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                non_duplicate_lst.append(nums[i+1])
        return non_duplicate_lst


print(Solution.remove_duplicates(None, nums=[1, 2, 2, 3, 3, 5, 5, 6]))


# class Solution:
#     def remove_duplicates(self, nums: List) -> List:
#         """
#         since it's a sorted list
#         we can remove the duplicates by recording indexes
#         """
#         idx_lst = list()
#         idx_lst.append(0)
#         for i in range(0, len(nums)-1):
#             if nums[i] != nums[i+1]:
#                 idx_lst.append(i+1)
#         idx_lst = [nums[x] for x in idx_lst]
#         return idx_lst


print(Solution.remove_duplicates(None, nums=[1, 2, 2, 3, 3, 5, 5, 6]))