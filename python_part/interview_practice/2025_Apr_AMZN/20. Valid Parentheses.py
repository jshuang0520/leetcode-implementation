# https://leetcode.com/problems/valid-parentheses/description/

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"{()}"
"""

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open = {'(', '[', '{'}
        close = {')', ']', '}'}
        hashmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = deque()

        for i in range(0, len(s)):
            if s[i] in open:
                stack.append(s[i])
            else:  # close bracket: let's match
                if not stack:  # FIXME: key point here! nothing to pop, since the close bracket comes first, and this is an unwanted pattern
                    return False
                o = stack.pop()
                if hashmap[s[i]] != o:
                    return False
        if stack:
            return False
        else:
            return True

strings = [
    "()", 
    "()[]{}", 
    "{()}", 
    "(]{}", 
    "}{", 
    "}["
]
sol = Solution()
for s in strings:
    print(f'string: {s}, ans: {sol.isValid(s=s)}')




