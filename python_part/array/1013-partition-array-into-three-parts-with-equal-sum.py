from typing import *


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        """
        if an array can be splitted into three parts and every part has the same value, it means we can check sum of the array, and the sum can be devided by 3

        also, the array is splitted into 3 parts in consecutive order, so we can check the index in order!

        ---
        Runtime 300 ms Beats 98.53% Memory 21.1 MB Beats 36.83%
        """
        n_times = 3
        arr_sum = sum(arr)
        ans = False

        if arr_sum % n_times == 0:
            target = arr_sum // n_times
            total = 0
            times_total_eq_target = 0

            for elem in arr:
                total += elem
                if total == target:  # key point
                    times_total_eq_target += 1
                    total = 0
                if times_total_eq_target == n_times:
                    ans = True
                    break
        return ans


# class Solution:
#     def canThreePartsEqualSum(self, arr: List[int]) -> bool:
#         """
#         if an array can be splitted into three parts and every part has the same value, it means we can check sum of the array, and the sum can be devided by 3
#
#         also, the array is splitted into 3 parts in consecutive order, so we can check the index in order!
#
#         ---
#         Runtime 337 ms Beats 54.14% Memory 20.9 MB Beats 79.37%
#         """
#         n_times = 3
#         arr_sum = sum(arr)
#         ans = False
#
#         if arr_sum % n_times == 0:
#             target = int(arr_sum / n_times)
#             total = 0
#             times_total_eq_target = 0
#
#             for i in range(0, len(arr)):
#                 total += arr[i]
#                 if total == target:  # key point
#                     times_total_eq_target += 1
#                     total = 0
#                 if times_total_eq_target == n_times:  # use "==" can get wrong ans
#                     ans = True
#                     break
#         return ans


# class Solution:
#     def canThreePartsEqualSum(self, arr: List[int]) -> bool:
#         """
#         if an array can be splitted into three parts and every part has the same value, it means we can check sum of the array, and the sum can be devided by 3
#
#         also, the array is splitted into 3 parts in consecutive order, so we can check the index in order!
#         ---
#
#         Runtime 335 ms Beats 58.1% Memory 21.1 MB Beats 6.45%
#         """
#         n_times = 3
#         arr_sum = sum(arr)
#         ans = False
#         if set(arr) == {0}:
#             ans = True
#         elif arr_sum % n_times == 0:
#             target = int(arr_sum / n_times)
#             total = 0
#             times_total_eq_target = 0
#
#             for i in range(0, len(arr)):
#                 total += arr[i]
#                 if total == target:  # key point
#                     times_total_eq_target += 1
#                     total = 0
#             if times_total_eq_target >= n_times:  # use "==" can get wrong ans
#                 ans = True
#         #     print(f'target: {target}')
#         # print(f'times_total_eq_target: {times_total_eq_target}')
#         # print(f'arr_sum: {arr_sum}')
#         # # print(f'arr_sum // n_times: {arr_sum // n_times}')
#         # print(f'arr_sum % n_times: {arr_sum % n_times}')
#         return ans