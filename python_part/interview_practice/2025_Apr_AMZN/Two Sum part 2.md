https://datalemur.com/questions

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

> ✅ method 2

Runtime 2 ms Beats 85.94% 

Memory 18.72 MB Beats 10.36%
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since it's sorted, we don't actually need binary search
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]
```

> method 1

Runtime 811 ms Beats 5.03%

Memory 18.60 MB Beats 34.06%
```python
class Solution:
    def binary_search(self, arr, target):
        """
        left, mid, right are index!
        """
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid  # found
            elif arr[mid] < target:
                left = mid + 1  # search right
            else:
                right = mid - 1  # search left
        return -1  # not found

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        constant extra space allowed
        """
        # since sorted, binary search is good
        for i in range(0, len(numbers)):
            diff = target - numbers[i]
            # search
            idx = self.binary_search(arr=numbers[i+1:], target=diff)
            if idx != -1:
                return [i+1, ((i+1)+(idx+1))]  # since in this problem, index starts from 1
        return [-1, -1]
```

https://datalemur.com/questions/python-two-sum-2

```python
def sorted_two_sum(nums, target):
    # since it's sorted, we don't actually need binary search
    left = 0
    right = len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]
```