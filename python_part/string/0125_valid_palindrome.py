# -*- coding: utf-8 -*-
from typing import List
from utility.utils import Logger, timeit

"""
String
0125	Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""


# Time: O(n)
# Space: O(1)


class Solution:
    def __init__(self):
        self.logger = Logger().get_logger('answer')

    @timeit
    def run(self, s: str) -> bool:
        """
        description:
        Given a string
        -> string
        --

        reference
        google: python remove all Punctuation Marks
        https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string

        This gives the following results:
        sets      : 19.8566138744
        regex     : 6.86155414581
        translate : 2.12455511093
        replace   : 28.4436721802
        --

        Runtime: 48 ms, faster than 58.35% of Python3 online submissions for Valid Palindrome.
        Memory Usage: 15.6 MB, less than 26.91% of Python3 online submissions for Valid Palindrome.
        """
        import string
        s = s.translate(str.maketrans('', '', string.punctuation))  # FIXME: using this method to remove punctuations is much faster than doing replace or even regex
        s = str(''.join(s.split(' '))).lower()
        self.logger.info('s: {}'.format(s))

        if len(s) == 1:
            return True
        else:
            # TODO: not really a todo, just a note - '// for quotients', '% for remainders'
            # if len(s) % 2 == 1:  # odd number
            #     num = len(s) // 2
            #     boolean_val = s[:num:] == s[-num::][::-1]
            #     return boolean_val
            num = len(s) // 2
            return s[:num:] == s[-num::][::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.run(s="A man, a plan, a canal: Panama"))
    print(sol.run(s="race a car"))
    print(sol.run(s="a."))
