from collections import Counter
from typing import *


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        plan:
        we do not sort,
        instead,
        we collect elements (through counting them, and then we append elements n times, to different lists, under circumstances)
        and finally, we concat the lists

        --
        Counter()
        in_arr2 = list()
        not_in_arr2 = list()
        """
        c = Counter()
        in_arr2 = list()
        not_in_arr2 = list()

        # Counter
        for elem in arr1:
            c[elem] += 1

        # collect element for in_arr2
        for i in range(0, len(arr2)):
            # element = arr2[i]
            # n_times = c[arr2[i]]
            in_arr2.extend([arr2[i]] * c[arr2[i]])  # python list repeat element n times

        # collect element for not_in_arr2
        diff = sorted(list(set(arr1) - set(arr2)))  # FIXME: "diff = list(set(arr1) - set(arr2))" leads to wrong order
        if diff:
            for x in diff:
                not_in_arr2.extend([x] * c[x])

            # update  # FIXME: wrong statement "in_arr2 = in_arr2.extend(not_in_arr2)" will lead in_arr2 to be None
            in_arr2.extend(not_in_arr2)  # -> correct statement to extend, update a list
        return in_arr2


print(Solution.relativeSortArray(None, arr1=[2,3,1,3,2,4,6,7,9,2,19], arr2=[2,1,4,3,9,6]))
