from typing import *
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tmp = Counter(words[0])
        for i in range(0, len(words)):
            tmp &= Counter(words[i])  # tmp = tmp.__iand__(Counter(words[i])) # in-place and
            # tmp = tmp.intersection(Counter(words[i])) # FIXME: wrong type
        return list(tmp.elements())


# # FIXME: use set => exclude duplicates
# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         for i in range(0, len(words)):
#             words[i] = set(list(words[i]))
#         for i in range(0, len(words)-1):
#             if i == 0:
#                 tmp = words[i].intersection(words[i+1])
#             else:
#                 tmp = tmp.intersection(words[i+1])
#         tmp = set(tmp)
#         return tmp
