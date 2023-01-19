from typing import *
from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        to store temp info into a data structure that data would be retrieved quickly in the future
        -> defaultdict
        """
        pairs = 0
        dd = defaultdict(int)
        # (n - target = k) or (n - target = -k)
        # => (target = n - k) or (target = n + k)
        for n in nums:
            dd[n] += 1
            pairs += dd[n-k] + dd[n+k]  # means: pairs += dd[target]  # see the comment above! (line 13)
        return pairs
