# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs):
        """ enhancement: to prevent from unnecessary dict creation, character ordering.
        since anagrams consist of same sets of characters, there is no need to actually count them, we just need to sort the characters, and the same anagrams will be in the same group
        --
        Runtime 11 ms Beats 80.28%
        Memory 19.56 MB Beats 87.19%
        """
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Runtime 51 ms Beats 5.74%
        Memory 20.61 MB Beats 40.26%
        """
        ans_dict = defaultdict(list)
        # {{"e":1, "a":1, "t":1}: ["eat"]} -> since key can not be a dictionary
        for string in strs:
            dd = defaultdict(int)
            for s in string:
                dd[s] += 1
            dd = dict(sorted(dd.items()))
            res = ''.join(str(key) + str(val) for key, val in dd.items())  # thus I turn the dictionary into a string
            ans_dict[res].append(string)
        print(ans_dict)
        return list(ans_dict.values())