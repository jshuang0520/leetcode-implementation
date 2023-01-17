"""
14 // 3 == 4 -> 最大的整數商 ([記] 14 / 3 == 4.66; 14 // 3 == 4 -> 多一刀把小數點切掉)
14 % 3  == 2 -> 看餘數 ([記] 「魚」 %%% -> 「餘」數)
"""

from functools import reduce
lst = [2, 3, 4]
ans = reduce(lambda x, y: x*y, lst)  # [python multiply elements in list](https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python)
print(f'ans: {ans}')
