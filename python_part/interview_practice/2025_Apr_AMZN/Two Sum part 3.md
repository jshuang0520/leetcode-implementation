https://datalemur.com/questions

- leetcode locked
https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://leetcode.com/problems/two-sum-iii-data-structure-design/&ved=2ahUKEwiP8YaTuOiMAxVGF1kFHQnsKt8QFnoECBwQAQ&usg=AOvVaw2n_-wRoZb-P_ARMXPOa63a

```python

```

https://datalemur.com/questions/python-two-sum-3

## notice

✅ nums.sort()  -> correct, due to no further assignment

❌ nums = nums.sort() -> wrong, since .sort() is an in-place replacement, so this assignment will make `nums` a `NonType` object

```python
def max_two_sum(nums, k):
  # nums = nums.sort()  # FIXME: error, since .sort() is an in-place replacement
  nums.sort()  # correct, due to no further assignment

  left = 0
  right = len(nums) - 1
  maxSum = 0
  while left < right:
    total = nums[left] + nums[right]
    if total < k:
      maxSum = max(maxSum, total)
      left += 1
    elif k <= total:
      right -= 1
  if maxSum:
    return maxSum

  return -1
```