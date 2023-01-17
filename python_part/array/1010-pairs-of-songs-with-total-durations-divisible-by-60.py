from typing import *
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # pairs -> defaultdict
        # divisible -> mod
        ans = 0
        dd = defaultdict(int)  # assign value type to "int"
        for t in time:
            if t % 60 == 0:
                t = 60
                ans += dd[t]
            else:
                t = t % 60
                ans += dd[60-t]
            dd[t] += 1
        return ans


# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solutions/2380490/python-with-simple-explanation-on-arriving-at-twosum-problem/
# [explanation_with_image](https://assets.leetcode.com/users/images/a7b12d6d-f136-4681-a03a-fbb4f97a62fc_1659648494.4292617.png)


# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solutions/2004218/python-sol-hashmap-mod-intution-explained-approach-explained/
"""


e.g.
Say we have a number 100 and another 140
100 is 60 + 40 , so to be divisible by 60 it needs number which will be 60x + 20
such that total = 60(x+1) + 40 + 20 = 60(x+2)

140 = 60 + 60 + 20 
So as 100 will require a number whose mod is 60 - 100%60 i.e. 20
100 + 140 = 240 which is divisible by 60
"""


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dd_map = defaultdict(int)
        ans = 0
        for t in time:
            if t % 60 == 0:
                t = 60
                ans += dd_map[60]
                # print(f'"if" - ans: {ans}; dd_map: {dd_map}')
            else:
                t = t % 60
                ans += dd_map[60-t]
                # print(f'"else" - ans: {ans}; dd_map: {dd_map}')
            dd_map[t] += 1
            print(f'"outside" - ans: {ans}; dd_map: {dd_map}')
            # print("----------------------------------")
        return ans


Solution.numPairsDivisibleBy60(None, time=[20,40, 20,40, 20,40, 40])
# Solution.numPairsDivisibleBy60(None, time=[30,20,150,100,40])


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        HashMap = {}
        pairs = 0
        for t in time:
            numMod = t % 60
            if numMod == 0:
                if 0 in HashMap:
                    pairs += HashMap[0]
            elif (60 - numMod) in HashMap:
                pairs += HashMap[60 - numMod]
            if numMod in HashMap:
                HashMap[numMod] += 1
            else:
                HashMap[numMod] = 1
            print(f'"outside" - HashMap: {HashMap}; pairs: {pairs}')
        print(f'pairs: {pairs}')
        return pairs


Solution.numPairsDivisibleBy60(None, time=[20,40, 20,40, 20,40, 40])

# # FIXME: this solution passed the example test case, but when we submit: Time Limit Exceeded -> too slow!
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         res = 0
#         for i in range(0, len(time)-1):
#             for j in range(i+1, len(time)):
#                 if (time[i] + time[j]) % 60 == 0:
#                     res += 1
#         return res
