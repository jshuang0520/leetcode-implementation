from typing import *
from collections import defaultdict


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """ to store info -> defaultdict
        {1個bit1: [1,2,4,8],
        2個bit1: [3,5,6],
        3個bit1: [7],
        }

        --
        num_wise  bit_wise
        0           0
        1           1
        2          10
        3          11
        4         100
        5         101
        """
        dd = defaultdict(list)  # type of value: list
        for x in arr:
            dd[bin(x).count("1")].append(x)

        # to get sorted "key"s
        sorted_keys = sorted(dd.keys())  # FIXME: do not sort a dictionary

        ans_list = list()
        for x in sorted_keys:
            ans_list += sorted(dd[x])
        return ans_list


# # FIXME: wrong answer
# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         """ to store info -> defaultdict
#         {1個bit1: [1,2,4,8],
#         2個bit1: [3,5,6],
#         3個bit1: [7],
#         }
#
#         --
#         num_wise  bit_wise
#         0           0
#         1           1
#         2          10
#         3          11
#         4         100
#         5         101
#         """
#         dd = defaultdict(list)  # type of value: list
#         for x in arr:
#             dd[bin(x).count("1")].append(x)
#         # sort by key
#         dd = sorted(dd)  # FIXME: do not sort a dictionary
#
#         ans_list = list()
#         for k, v in dd.items():
#             ans_list += sorted(v)
#         return ans_list


# # FIXME: wrong answer
# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         # target_set with 2^n values
#         target_set = set()
#         for i in range(0, 1000):
#             value = 2 ** i
#             if value <= 10 ** 4:
#                 target_set.add(value)
#         target_set.add(0)  # [0] is the only integer with 0 bits.
#
#         in_2_power = list()
#         not_in_2_power = list()
#         for x in arr:
#             if x in target_set:
#                 in_2_power.append(x)
#             else:
#                 not_in_2_power.append(x)
#         return sorted(in_2_power) + sorted(not_in_2_power)
#
#
# print(Solution.sortByBits(None, arr=[2,3,5,7,11,13,17,19]))
# """ wrong answer
# Output
# [2,3,5,7,11,13,17,19]
# Expected
# [2,3,5,17,7,11,13,19]
# """
