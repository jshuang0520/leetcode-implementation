from typing import *
from collections import Counter, defaultdict


# sol 2 - my own solution - Runtime 38 ms Beats 98.95%, Memory 13.9 MB Beats 59.91%
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """concept
        store info and retrieve quickly -> defaultdict
          - (auxiliary): use counter to count occurrences for each alphabet
          - how to store info:
            {"alphabet_1": [occurrences_in_str_1, occurrences_in_str_2, occurrences_in_str_3],
             "alphabet_2": [occurrences_in_str_1, occurrences_in_str_2, occurrences_in_str_3],
             "alphabet_3": [occurrences_in_str_2, occurrences_in_str_3],
            } -> note. length of values can be different, because not all strings contain all of the alphabets
        """
        ans_lst = list()
        len_words = len(words)
        dd = defaultdict(list)

        for word in words:
            cnt = Counter(word)
            for k, v in dict(cnt).items():
                dd[k].append(v)
        for k, v in dd.items():
            if len(v) != len_words:
                pass
            else:
                ans_lst += [k] * min(v)

        return ans_lst


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
