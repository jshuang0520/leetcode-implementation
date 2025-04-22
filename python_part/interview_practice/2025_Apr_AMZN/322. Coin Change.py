from typing import List

class Solution:
    def binary_search(self, arr, target):
        """
        to find the closed right index for further searching
        """
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        sort arr
        use Binary Search to find right_idx
        mark right_idx to be where to start: the element < amount
        cnt = 0
        loop
          if arr[right_idx] <= amount:
            times = amount // element
            amount -= element * times
            cnt += times
            right_idx -= 1
        """
        if amount == 0:
            return 0
        
        # (coins).sort()

        # find right_idx to start: via binary search
        right_idx = self.binary_search(arr=coins, target=amount)
        # fewest coin changes
        cnt = 0
        # need to update amount
        while right_idx >= 0 and amount > 0:
            if right_idx == 0 and amount % coins[0] != 0:
                return -1
            # print(f'right_idx: {right_idx}')
            elem = coins[right_idx]
            # print(f'elem: {elem}')
            if elem <= amount:
                times = amount // elem
                amount -= elem * times
                cnt += times
                # print(f'cnt: {cnt}')
            right_idx = self.binary_search(arr=coins, target=amount)
            # print(f'after right_idx: {right_idx}')
            # print(f'amount: {amount}')
            # print('--')
            if right_idx <= 1:
                right_idx -= 1
        
        return cnt

"""
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
 
Test 10:
coins = [1,2147483647], amount = 2

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

sol = Solution()

coins = [1,2,5]
amount = 11
print(sol.coinChange(coins=coins, amount=amount))

coins = [2]
amount = 3
print(sol.coinChange(coins=coins, amount=amount))


coins = [1]
amount = 0
print(sol.coinChange(coins=coins, amount=amount))


coins = [1,2147483647]
amount = 2
print(sol.coinChange(coins=coins, amount=amount))