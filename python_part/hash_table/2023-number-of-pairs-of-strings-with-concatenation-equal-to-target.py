from collections import defaultdict
from typing import *
import math
from collections import Counter


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        """
        to store meta data -> think of dictionary
        refer to: https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/solutions/1499007/python3-freq-table/?orderBy=most_votes&languageTags=python3
        --
        Runtime 45 ms Beats 78.39% Memory 13.9 MB Beats 64.44%
        """
        nums_counter = Counter(nums)
        ans = 0

        for key, value in nums_counter.items():
            if target.startswith(key):  # this string .startswith() method is better, because there are more details to be concerned when using .replace('from_this', 'to_this', 1) -> replace ONLY ONCE: first occurrence
                counterpart_key = target[len(key):]  # by retrieving the rest of the characters, we don't have to worry about issues when using .replace()
                # print(f'counterpart_key: {counterpart_key}')
                ans += value * nums_counter[counterpart_key]
                if key == counterpart_key:  # TODO read this -> QUESTION: why is it (n^2 - n)? According to the description "return the number of pairs of indices (i, j) (where i != j)" -> "where i != j"is why we minus n -> KEYPOINT: should be (n^2 - n), not factorial answer, and we've done n^2 on the above line, thus we need to do minus n part here. e.g. when nums=["777","7","77","77"], target="7777" -> "77": 2^2 - 2 = 2; when nums=["1","1","1"], target="111" -> "1": 3^2 - 3 = 6 -> I've once misunderstood it as a factorial answer!
                    ans -= value
        return ans


# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """
#         to store meta data -> think of dictionary
#         refer to: https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/solutions/1499007/python3-freq-table/?orderBy=most_votes&languageTags=python3
#         --
#         Last Executed Input
#         104 / 117 testcases passed
#         nums =
#         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
#         target =
#         "11"
#         """
#         nums_counter = Counter(nums)
#         ans = 0
#
#         for key, value in nums_counter.items():
#             if target.startswith(key):  # this string .startswith() method is better, because there are more details to be concerned when using .replace('from_this', 'to_this', 1) -> replace ONLY ONCE: first occurrence
#                 counterpart_key = target[len(key):]  # by retrieving the rest of the characters, we don't have to worry about issues when using .replace()
#                 print(f'counterpart_key: {counterpart_key}')
#                 if key == counterpart_key:  # factorial answer, e.g. when nums=["777","7","77","77"], target="7777" -> "77": 2! = 2; when nums=["1","1","1"], target="111" -> "1": 3! = 6
#                     if nums_counter[key] == 1:
#                         ans += 0
#                     else:
#                         ans += math.factorial(nums_counter[key])
#                 else:
#                     ans += value * nums_counter[counterpart_key]
#         return ans


nums = ["777","7","77","77"]
target = "7777"
print(f'nums: {nums}, target: {target}')
print('numOfPairs:', Solution.numOfPairs(None, nums, target), '\n')

nums = ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
target = "11"
print(f'nums: {nums}, target: {target}')
print('numOfPairs:', Solution.numOfPairs(None, nums, target), '\n')
# wrong ans: numOfPairs: 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
# correct ans: numOfPairs: 9900


# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """
#         to store meta data -> think of dictionary
#         refer to: https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/solutions/1499007/python3-freq-table/?orderBy=most_votes&languageTags=python3
#         """
#         nums_counter = Counter(nums)
#         ans = 0
#
#         for key, value in nums_counter.items():
#             if target.startswith(key):  # this string .startswith() method is better, because there are more details to be concerned when using .replace('from_this', 'to_this', 1) -> replace ONLY ONCE: first occurrence
#                 counterpart_key = target[len(key):]  # by retrieving the rest of the characters, we don't have to worry about issues when using .replace()
#                 if key == counterpart_key:  # just double counted, so we need to minus it, e.g. when nums=["777","7","77","77"], target="7777" -> "77" will be double counted
#                     ans += math.factorial(nums_counter[key])
#                 else:
#                     ans += value * nums_counter[counterpart_key]
#         return ans


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        """
        to store meta data -> think of dictionary
        refer to: https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/solutions/1499007/python3-freq-table/?orderBy=most_votes&languageTags=python3
        --
        Runtime 41 ms Beats 87.76% Memory 13.9 MB Beats 94.7%
        """
        nums_counter = Counter(nums)
        ans = 0

        for key, value in nums_counter.items():
            if target.startswith(key):  # this string .startswith() method is better, because there are more details to be concerned when using .replace('from_this', 'to_this', 1) -> replace ONLY ONCE: first occurrence
                counterpart_key = target[len(key):]  # by retrieving the rest of the characters, we don't have to worry about issues when using .replace()
                ans += value * nums_counter[counterpart_key]
                if key == counterpart_key:  # (n^2 - n) -> just counted the duplicates, so we need to do the minus n part , e.g. when nums=["777","7","77","77"], target="7777" -> "77" will be double counted
                    ans -= nums_counter[counterpart_key]
        return ans


nums = ["777","7","77","77"]
target = "7777"
print(f'nums: {nums}, target: {target}')
print('numOfPairs:', Solution.numOfPairs(None, nums, target), '\n')

nums = ["1","111"]
nums = ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
target = "11"
print(f'nums: {nums}, target: {target}')
print('numOfPairs:', Solution.numOfPairs(None, nums, target), '\n')


# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """ wrong answer
#         to store meta data -> think of dictionary
#
#         --
#         Input
#         nums =
#         ["123","4","12","34"]
#         target =
#         "1234"
#         Output
#         4
#         Expected
#         2
#         """
#         dd = defaultdict(list)
#         ans = 0
#         # dd[target.replace(num, '')] += 1
#
#         for idx, num in enumerate(nums):
#             dd[num].append(idx)
#
#         keys_set = set(dd.keys())
#         for key, value in dd.items():
#             counterpart_key = target.replace(key, '', 1)  # replace only once!
#             # print(f'counterpart_key: {counterpart_key}')
#
#             if (key in keys_set) and (counterpart_key in keys_set):
#                 if key * 2 == target:
#                     ans += math.factorial(len(dd[key]))
#                 else:
#                     if target + target[::-1] == target[::-1] + target: # if the string is symmetric
#                         # ans += (len(dd[key]) * len(dd[counterpart_key])) / 2  # consider duplicates when iter whole list
#                         ans += len(dd[key])
#                     else:
#                         ans += len(dd[counterpart_key])
#                 # print(f'key: {key}, value: {value}, ans: {ans}')
#         return int(ans)
#
#
# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """ wrong answer
#         to store meta data -> think of dictionary
#
#         --
#         Input
#         nums =
#         ["1","111"]
#         target =
#         "11"
#         34 / 117 testcases passed
#         Output
#         1
#         Expected
#         0
#         """
#         dd = defaultdict(list)
#         ans = 0
#         # dd[target.replace(num, '')] += 1
#
#         for idx, num in enumerate(nums):
#             dd[num].append(idx)
#
#         keys_set = set(dd.keys())
#         for key, value in dd.items():
#             counterpart_key = target.replace(key, '', 1)  # replace only once!
#             # print(f'counterpart_key: {counterpart_key}')
#
#             if (key in keys_set) and (counterpart_key in keys_set):
#                 if key * 2 == target:
#                     ans += math.factorial(len(dd[key]))
#                 else:
#                     if target + target[::-1] == target[::-1] + target:  # if the string is symmetric
#                         ans += len(dd[key])
#                     else:
#                         ans += len(dd[key]) / 2
#                 # print(f'key: {key}, value: {value}, ans: {ans}')
#         return int(ans)
#
#
# nums = ["777","7","77","77"]
# target = "7777"
# print(f'nums: {nums}, target: {target}')
# print('numOfPairs:', Solution.numOfPairs(None, nums, target), '\n')
#
# nums = ["123","4","12","34"]
# target = "1234"
# print(f'nums: {nums}, target: {target}')
# print('numOfPairs:', Solution.numOfPairs(None, nums, target), '\n')
#
# nums = ["1","1","1"]
# target = "11"
# print(f'nums: {nums}, target: {target}')
# print('numOfPairs:', Solution.numOfPairs(None, nums, target), '\n')
#
# nums = ["1","111"]
# target = "11"
# print(f'nums: {nums}, target: {target}')
# print('numOfPairs:', Solution.numOfPairs(None, nums, target), '\n')
#
#
# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """ wrong answer
#         to store meta data -> think of dictionary
#
#         階乘 math.factorial(x)
#         """
#         dd = defaultdict(list)
#         ans = 0
#         # dd[target.replace(num, '')] += 1
#
#         for idx, num in enumerate(nums):
#             dd[num].append(idx)
#
#         keys_set = set(dd.keys())
#         for key, value in dd.items():
#             counterpart_key = target.replace(key, '', 1)  # replace only once!
#             # print(f'counterpart_key: {counterpart_key}')
#             if (key in keys_set) and (counterpart_key in keys_set):
#                 ans += (len(dd[key]) * len(dd[counterpart_key])) / 2  # consider duplicates when iter whole list
#         return ans
#
#
# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """ wrong answer
#         to store meta data -> think of dictionary
#
#         階乘 math.factorial(x)
#         """
#         dd = defaultdict(list)
#         ans = 0
#         # dd[target.replace(num, '')] += 1
#
#         for idx, num in enumerate(nums):
#             dd[num].append(idx)
#
#         keys_set = set(dd.keys())
#         for key, value in dd.items():
#             counterpart_key = target.replace(key, '', 1)  # replace only once!
#             # print(f'counterpart_key: {counterpart_key}')
#             if (key in keys_set) and (counterpart_key in keys_set):
#                 ans += (math.factorial(
#                     len(dd[key]) * len(dd[counterpart_key]))) / 2  # consider duplicates when iter whole list
#         return ans
#
#
# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """ wrong answer
#         to store meta data -> think of dictionary
#
#         階乘 math.factorial(x)
#         """
#         dd = defaultdict(list)
#         ans = 0
#         # dd[target.replace(num, '')] += 1
#
#         for idx, num in enumerate(nums):
#             dd[num].append(idx)
#
#         keys_set = set(dd.keys())
#         for key, value in dd.items():
#             counterpart_key = target.replace(key, '')  # FIXME: this will replace all of them
#             # print(f'counterpart_key: {counterpart_key}')
#             if (key in keys_set) and (counterpart_key in keys_set):
#                 ans += (math.factorial(
#                     len(dd[key]) * len(dd[counterpart_key]))) / 2  # consider duplicates when iter whole list
#         return ans
#
#
# # # TODO: important information
# # dd = {'777': [0], '7': [1], '77': [2, 3]}
# # target = '7777'
# # for key, value in dd.items():
# #     counterpart_key = target.replace(key, '')
# #     print(f'key: {key}')
# #     print(f'counterpart_key: {counterpart_key}')
# #     print(f'target: {target}')
# '''
# target: 7777
# key: 777
# counterpart_key: 7
#
# target: 7777
# key: 7
# counterpart_key:              ---------------------> 'a bug' due to string replace method !!!!!!!!!!
#
# target: 7777
# key: 77
# counterpart_key:              ---------------------> 'a bug' due to string replace method !!!!!!!!!!
# '''
#
#
# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """ wrong answer
#         to store meta data -> think of dictionary
#         """
#         dd = defaultdict(int)
#         ans = 0
#
#         for num in nums:
#             # dd[target.replace(num, '')] += 1
#             ans += dd[num]
#             ans += dd[target.replace(num, '')]
#             dd[num] += 1
#         return ans
#
#
# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         """ wrong answer
#         to store meta data -> think of dictionary
#         """
#         dd = defaultdict(int)
#         ans = 0
#
#         for num in nums:
#             # dd[target.replace(num, '')] += 1
#             if num in target:
#                 ans += dd[num]
#             else:
#                 ans += dd[target.replace(num, '')]
#             dd[num] += 1
#         return ans
