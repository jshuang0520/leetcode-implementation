from typing import *


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        ---
        Runtime 71 ms Beats 79.52% Memory 14.9 MB Beats 61.29%
        """
        arr_len = len(arr)

        i = 0
        while i < arr_len:
            if arr[i] == 0:
                arr.insert(i, 0)
                del arr[-1]
                i += 2
            else:
                i += 1


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        --
        Runtime 75 ms Beats 64.83% Memory 14.9 MB Beats 20.48%
        """
        target_idx_lst = list()
        shift_cnt = 0
        arr_len = len(arr)

        for i in range(len(arr)):
            if arr[i] == 0:
                if i + shift_cnt < arr_len:
                    target_idx_lst.append(i + shift_cnt)
                    shift_cnt += 1
        for idx in target_idx_lst:
            arr.insert(idx, 0)
            del arr[-1]


# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """ wrong answer
#         Do not return anything, modify arr in-place instead.
#         --
#         Input
#         arr =
#         [1,0,2,3,0,4,5,0]
#         Output
#         [1,0,0,2,3,0,0,4,5,0,0]
#         Expected
#         [1,0,0,2,3,0,0,4]
#         """
#         target_idx_lst = list()
#         shift_cnt = 0
#
#         for i in range(len(arr)):
#             if arr[i] == 0:
#                 target_idx_lst.append(i + shift_cnt)
#                 shift_cnt += 1
#         for idx in target_idx_lst:
#             arr.insert(idx, 0)
