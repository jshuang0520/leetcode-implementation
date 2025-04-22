# Efficient Search in Integer Arrays
# https://platform.stratascratch.com/algorithms/10383-efficient-search-in-integer-arrays?code_type=2

def max_subarray(arr):
    """thoughts
    track: running info and best info
    info: start / end idx, and sum
    update them
    """
    # FIXME: best_sum should be set to the first element of the arr
    # best_sum = 0
    best_sum       = arr[0]
    best_start_idx = best_end_idx = 0

    running_sum = arr[0]
    running_start_idx = 0

    for i in range(1, len(arr)):
        # check running status: to further determine if it is worth recording (the record high)
        # if running_sum <= 0:
        if running_sum < 0:
            # FIXME: didn't update running_sum
            running_sum = arr[i]
            running_start_idx = i
        else:
            running_sum += arr[i]
        
        # update the best
        if running_sum > best_sum:
            best_sum = running_sum
            best_start_idx = running_start_idx
            best_end_idx = i
        # return [best_sum, best_start_idx, best_end_idx]  # FIXME: notice the indent
    return [best_sum, best_start_idx, best_end_idx]


def max_subarray(arr):
    """ 
    :type input: List[int]
    :rtype: List[int] 
    """
    # “Best ever” (global to this function)
    best_total     = arr[0]
    best_start_idx = best_end_idx = 0

    # “Current run” (local, reset when negative)
    running_total  = arr[0]
    run_start_idx  = 0

    for i in range(1, len(arr)):
        # Restart if the run so far is negative
        if running_total < 0:               # Restart condition
            running_total  = arr[i]         # running_total
            run_start_idx  = i              # run_start_idx
        else:
            running_total += arr[i]         # green light, keep going

        # Record a new overall best
        if running_total > best_total:      # keep updating the record high
            best_total     = running_total  # running_total
            best_start_idx = run_start_idx  # run_start_idx
            best_end_idx   = i              # best_end_idx

    return [best_total, best_start_idx, best_end_idx]


print(max_subarray(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray(arr=[1, 2, 3, 4, 5]))
print(max_subarray(arr=[-1, -2, -3, -4, -5]))
print(max_subarray(arr=[5, -2, 3, -1, 2, -1, 2, -3, 4]))
print(max_subarray(arr=[0, -3, 1, -2, 3, 4, -1, 2, 1]))

"""
Test Case #1

Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: [6, 3, 6]
Description: The maximum sum is found in the subarray [4, -1, 2, 1], resulting in a sum of 6, starting at index 3 and ending at index 6.
Test Case #2

Input: [1, 2, 3, 4, 5]
Output: [15, 0, 4]
Description: The entire array is the maximum subarray with a sum of 15, starting at index 0 and ending at index 4.
Test Case #3

Input: [-1, -2, -3, -4, -5]
Output: [-1, 0, 0]
Description: The maximum sum is -1, which is the first element of the array. The subarray starts and ends at index 0.
Test Case #4

Input: [5, -2, 3, -1, 2, -1, 2, -3, 4]
Output: [8, 0, 8]
Description: The maximum sum is found in the subarray [5, -2, 3, -1, 2, -1, 2, -3, 4], resulting in a sum of 8, starting at index 0 and ending at index 8.
Test Case #5

Input: [0, -3, 1, -2, 3, 4, -1, 2, 1]
Output: [9, 2, 8]
Description: The maximum sum is found in the subarray [1, -2, 3, 4, -1, 2, 1], resulting in a sum of 9, starting at index 2 and ending at index 8.
"""