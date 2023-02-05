from typing import *
from collections import defaultdict


class Solution:
    """
    Runtime 159 ms Beats 85.58% Memory 15.8 MB Beats 87.73%
    """
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def dist(point):
            pi, pj = point
            return abs(pi - rCenter) + abs(pj - cCenter)

        points = [(i, j) for i in range(rows) for j in range(cols)]
        return sorted(points, key=lambda row: dist(point=row))  # a more readable version from this syntax: sorted(points, key=dist)


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        """
        this method sort those points:
        step1. collect all the points
        step2. sort elements(points) in a list, by dist = abs(pi - rCenter) + abs(pj - cCenter),
               thus we need to use the syntax: sorted(points, key=dist)

        google: python list most efficient sort
               note1. https://stackoverflow.com/questions/65352078/what-is-the-most-efficient-way-to-sort-an-array-with-the-first-item

               note2. [check the figure](https://i.stack.imgur.com/fEGCg.png)
                      https://stackoverflow.com/questions/3855537/fastest-way-to-sort-in-python

        ---
        Runtime 165 ms Beats 70.18% Memory 15.7 MB Beats 87.95%
        """
        def dist(point):
            pi, pj = point
            return abs(pi - rCenter) + abs(pj - cCenter)

        points = [(i, j) for i in range(rows) for j in range(cols)]
        return sorted(points, key=dist)  # google: python list most efficient sort (refer to notes above)  # TODO: improve it in next version


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        """
        this method sort the dictionary

        ---
        Runtime 171 ms Beats 58.74% Memory 15.9 MB Beats 64.16%
        """
        dd = defaultdict(list)
        ans_lst = list()

        for r in range(0, rows):
            for c in range(0, cols):
                dist = abs(r-rCenter) + abs(c-cCenter)  # |r1 - r2| + |c1 - c2|
                dd[dist].append([r,c])
                # if c > r: # upper triangular matrix  # FIXME: this restriction can lose some candidates
                #     break
        sorted_dict = dict(sorted(dd.items()))
        for key, value in sorted_dict.items():
            ans_lst.extend(value)
        return ans_lst


# rCenter=2
# cCenter=4
# def dist(point):
#     pi, pj = point
#     return abs(pi - rCenter) + abs(pj - cCenter)
#
#
# points = [[1,2], [3,4], [1,3], [1,4]]
# # print(sorted(points, key=dist))
# print(sorted(points, key=lambda row: dist(point=row)))
