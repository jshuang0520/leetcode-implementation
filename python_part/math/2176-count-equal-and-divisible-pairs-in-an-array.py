from typing import *
from collections import defaultdict
from functools import reduce

from collections import defaultdict
from functools import reduce


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # with param "k" -> need to be careful: because when using k,v for dict.items(), you will overwrite the param
        """
        find pairs in an array
        -> we need a data structure to store info and still data can be retrieved quickly in the future
        -> defaultdict: key -> hash table
        """
        ans = 0

        dd = defaultdict(list)  # value type: list (to collect int)
        for idx, n in enumerate(nums):
            dd[n].append(idx)
        # print(f'dd: {dd}')

        for key, value in dd.items():
            if (len(value) == 0) or (len(value) == 1):
                pass
            else:
                for i in range(0, len(value) - 1):
                    for j in range(i + 1, len(value)):
                        # print(f'key,value: {key, value} - value[i]: {value[i]}, v[j]: {value[j]}')
                        if value[i] * value[j] % k == 0:
                            # print(f'True: (value[{i}] * value[{j}]) % k == {(value[i] * value[j]) % k}')
                            ans += 1
                        # print(f'ans: {ans}')
        return ans


# class Solution:
#     def countPairs(self, nums: List[int], k: int) -> int:
#         """
#         find pairs in an array
#         -> we need a data structure to store info and still data can be retrieved quickly in the future
#         -> defaultdict: key -> hash table
#
#         ---
#         6 // 2 == 3 -> 整除後最大的商
#         6 % 2  == 0 -> 看餘數
#         """
#         ans = 0
#         dd = defaultdict(list)  # value type: list (to collect int)
#         for idx, n in enumerate(nums):
#             dd[n].append(idx)
#         for k, v in dd.items():
#             mul_res = reduce(lambda x, y: x*y, v)  # python multiply elements in list
#             if mul_res % k == 0:
#                 ans += 1
#         print(f'ans: {ans}')
#         return ans


Solution.countPairs(None, nums=[3,1,2,2,2,1,3], k=2)
