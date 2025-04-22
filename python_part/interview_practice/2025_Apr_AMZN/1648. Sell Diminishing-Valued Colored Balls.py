# from typing import List
# from collections import Counter
# import heapq

# def maxProfit(inventory: List[int], orders: int) -> int:
#     MOD = 10**9+7

#     # 1) Count identical heights, build max‑heap of (-value, count)
#     cnt = Counter(inventory)
#     heap = [(-v, c) for v, c in cnt.items()]
#     heapq.heapify(heap)

#     res = 0
#     while orders > 0 and heap:
#         # 2) Pop top group
#         neg_v1, c1 = heapq.heappop(heap)
#         v1 = -neg_v1

#         # 3) Peek next height
#         if heap:
#             v2 = -heap[0][0]
#         else:
#             v2 = 0

#         diff = v1 - v2
#         batch_size = diff * c1

#         if orders >= batch_size:
#             # take full batch
#             # sum of values from v1 down to v2+1 for one pile:
#             sum1 = (v1 + (v2 + 1)) * diff // 2
#             res = (res + sum1 * c1) % MOD
#             orders -= batch_size

#             # merge piles at v2
#             if heap:
#                 _, c2 = heapq.heappop(heap)
#                 c1 += c2
#             # push the merged group back at height v2
#             heapq.heappush(heap, (-v2, c1))

#         else:
#             # partial: only enough orders to take some levels + remainder
#             full_levels = orders // c1
#             rem = orders % c1
#             low = v1 - full_levels

#             # sum for full_levels layers:
#             sum_full = (v1 + (low + 1)) * full_levels // 2
#             res = (res + sum_full * c1) % MOD

#             # remainder balls at height 'low'
#             res = (res + rem * low) % MOD

#             orders = 0

#     return res


from typing import List

def maxProfit(inventory: List[int], orders: int) -> int:
    MOD = 10**9 + 7
    # 1. sort descending, append 0
    inventory.sort(reverse=True)
    inventory.append(0)
    
    res = 0
    n = len(inventory)
    i = 0
    
    # 2. process in batches
    while orders > 0:
        height = inventory[i]
        next_h = inventory[i+1]
        width = i + 1              # how many piles at this height
        diff = height - next_h     # how many levels we can drop
        
        full_batch = width * diff
        if orders >= full_batch:
            # take the entire batch: sum(height down to next_h+1) × width
            # sum of AP: (first + last) * count // 2
            batch_sum = (height + (next_h + 1)) * diff // 2
            res = (res + batch_sum * width) % MOD
            orders -= full_batch
            i += 1
        else:
            # we can only take part of this batch
            layers = orders // width
            rem    = orders % width
            # 1) take 'layers' full levels:
            #    sum from height down to height-layers+1
            full_sum = (height + (height - layers + 1)) * layers // 2
            res = (res + full_sum * width) % MOD
            # 2) take the remainder 'rem' at the next level
            res = (res + rem * (height - layers)) % MOD
            orders = 0

    return res


print(maxProfit(inventory=[1000000000], orders=1000000000))
