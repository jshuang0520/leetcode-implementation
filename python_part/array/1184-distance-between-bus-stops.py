from typing import *


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """
        it means we split the list into two parts:
        part1. lst[start:destination]
        part2. and the rest

        since the index start can > or = or < destination, there are various forms we have to deal with
        let's try this:
        --
        Runtime 47 ms Beats 75.98% Memory 14.9 MB Beats 46.65%
        """
        d1 = 0
        d2 = 0
        if start < destination:
            pass
        elif start == destination:
            return 0
        else:
            start, destination = destination, start

        for idx in range(start, destination):
            d1 += distance[idx]
            distance[idx] = 0
        return min(d1, sum(distance))


# class Solution:
#     def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
#         """ wrong answer
#         Input
#         distance =
#         [14,13,4,7,10,17,8,3,2,13]
#     idx  0  1  2 3 4  5  6 7 8 9
#         start =
#         2
#         destination =
#         9
#         28 / 37 testcases passed
#         Output
#         13
#         Expected
#         40
#         """
#         if start < destination:
#             return min(sum(distance[start:destination]), sum(distance[destination:]))
#         elif start == destination:
#             return 0
#         else:
#             return min(sum(distance[start:])+sum(distance[0:destination]), sum(distance[destination:start]))


# class Solution:
#     def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
#         """
#         I realize start and destination means 'index', not 'value'
#
#         --
#         wrong answer
#         Input
#         distance =
#         [3,6,7,2,9,10,7,16,11]
#         start =
#         6
#         destination =
#         2
#         7 / 37 testcases passed
#         Output
#         9
#         Expected
#         28
#         """
#         return min(sum(distance[0:destination]), sum(distance[destination:]))
#
#
# class Solution:
#     def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
#         """ wrong answer
#         distance =
#         [7,6,3,0,3]
#         start =
#         0
#         destination =
#         4
#         3 / 37 testcases passed
#         Output
#         0
#         Expected
#         3
#         """
#         if destination in set(distance):
#             d1 = 0
#             d2 = 0
#             for i in range(len(distance)):
#                 if distance[i] != destination:
#                     d1 += distance[i]
#                 else:
#                     d1 += distance[i]
#                     continue_idx = i + 1
#                     break
#             for i in range(continue_idx, len(distance)):
#                 d2 += distance[i]
#             return min(d1, d2)
#         else:
#             return 0
#
#
# class Solution:
#     def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
#         """ wrong answer
#         last Executed Input
#         3 / 37 testcases passed
#         distance =
#         [7,6,3,0,3]
#         start =
#         0
#         destination =
#         4
#         """
#         d1 = 0
#         d2 = 0
#         for i in range(len(distance)):
#             if distance[i] != destination:
#                 d1 += distance[i]
#             else:
#                 d1 += distance[i]
#                 continue_idx = i + 1
#                 break
#         for i in range(continue_idx, len(distance)):
#             d2 += distance[i]
#         return min(d1, d2)


arr = [0,1,2,3,4,5]
print(arr[0:3])
# [0, 1, 2]
