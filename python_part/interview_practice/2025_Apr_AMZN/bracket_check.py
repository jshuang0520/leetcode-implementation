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

# def check(string: str) -> bool:
#     dd = {
#         ')': '(',
#         '}': '{',
#         ']': '['
#         }
#     stack = list(string)
#     for _ in stack:
#         tmp = stack.pop()
#         if not dd[tmp]:
#             return False
#     return True

def check(string: str) -> bool:
    if len(string) % 2 != 0:
        return False
    open = {'(', '{', '['}
    closed =  {')', '}', ']'}
    t1 = {'(', ')'}
    t1 = {'(', ')'}
    t1 = {'(', ')'}
    dd = {
        '(': ')',
        '{': '}',
        '[': ']',
        ')': '(',
        '}': '{',
        ']': '['
        }
    stack = list(string)
    for i in range(0, len(stack)-1):
        if string[i+1]

        tmp = stack.pop()
        if not dd[tmp]:
            return False
    return True

s = "()"
s = "()[]{}"
s = "{()}"
print(check(string=s))



