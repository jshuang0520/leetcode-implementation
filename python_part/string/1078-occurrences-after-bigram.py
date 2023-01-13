from typing import *


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = list()
        lst = text.split(" ")
        for i in range(0, len(lst)-1):
            if (lst[i] == first) and (lst[i+1] == second):
                if i == len(lst)-2:
                    break
                else:
                    res.append(lst[i+2])
        return res
