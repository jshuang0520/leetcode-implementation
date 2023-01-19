# from collections import Counter
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        `t divides s if and only if s = t + ... + t`
        -> that is to say, there are no alphabets other than t in s

        according to this description, when we concat str1 and str2,
        it should be like a mirror, whether "str1+str2" or "str2+str1"
        or else, those two strings don't have gcd in common
        """
        ans = ""
        if (str1 + str2) == (str2 + str1):
            ans = str1[:gcd(len(str1), len(str2))]

        return ans


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[:gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ''


""" explanation
https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/860984/python-3-gcd-1-liner-explanation/?orderBy=most_votes&languageTags=python
"""

# # FIXME: "ABCDEF", "ABC" -> expect: ""; my_ans: "ABC"
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         len1 = len(str1)
#         len2 = len(str2)
#         num = min(len1, len2)
#         if str1[0:num] != str2[0:num]:
#             return ""
#         else:
#             length_by_gcd = gcd( len(str1), len(str2) )
#             return str1[:length_by_gcd]


# # FIXME: case 2 return "ABAB", there's a duplicate, so it is not gcd
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         len1 = len(str1)
#         len2 = len(str2)
#         num = min(len1, len2)
#         if str1[0:num] != str2[0:num]:
#             return ""
#         else:
#             return str1[0:num]


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         len1 = len(str1)
#         len2 = len(str2)
#         num = min(len1, len2)
#         if str1[0:num] != str2[0:num]:
#             return ""
#         else:
#             tmp = str1[0:num]
#             c = dict(Counter(list(tmp)))
#             for k,v in c.items():
#                 if v > 1

#             return


# # FIXME: 順序不同、"LEET","CODE"也會找到"E"，但並非 common divisor of string
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         set1 = set(list(str1))
#         set2 = set(list(str2))
#         tmp = set1.intersection(set2)
#         return "".join(tmp)
