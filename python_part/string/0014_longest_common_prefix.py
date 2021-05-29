# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit

"""
String
0014	Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""


# Time:  O(n * k)
# Space: O(1)


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @timeit
    def run(self, strs: List[str]) -> str:
        """
        reference
        google: python list of string common prefix
        https://stackoverflow.com/questions/61788169/how-to-get-common-prefix-of-strings-in-a-list
        --

        Runtime: 36 ms, faster than 50.89% of Python3 online submissions for Longest Common Prefix.
        Memory Usage: 14.2 MB, less than 80.41% of Python3 online submissions for Longest Common Prefix.
        """
        '''
        log printed:
        s: ('f', 'f', 'f')
        s: ('l', 'l', 'l')
        ------------------- -> the conditional flow breaks here
        s: ('o', 'o', 'i')
        s: ('w', 'w', 'g')
        '''
        res = list()
        for s in zip(*strs):  # FIXME: the usage of zip for all elements in a list, check the log printed above
            if len(set(s)) == 1:
                self.logger.info('s: {}'.format(s))
                res.append(s[0])
            else:
                break

        if len(res) == 0:
            return ''
        else:
            return ''.join([x for x in res])


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(strs=["flower", "flow", "flight"]))
    print(sol.run(strs=["dog", "racecar", "car"]))
