https://datalemur.com/questions

https://leetcode.com/problems/two-sum/description/

✅
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()  # key: num, val: its idx
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            seen[nums[i]] = i
        return [-1, -1]
```

https://datalemur.com/questions/python-two-sum

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    diff_set = set()
    for i in range(0, len(nums)):
      diff_set.add(target-nums[i])
    for i in range(0, len(nums)):
      if nums[i] in diff_set:
        if i == nums.index(target-nums[i]):
          pass
        else:
          return sorted([i, nums.index(target-nums[i])])
    return [-1, -1]
```