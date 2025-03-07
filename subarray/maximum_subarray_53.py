def max_subarray(nums):
    cur_sum = max_sum = nums[0]
    for val in nums[1:]:
        cur_sum = max(cur_sum + val, val)
        # cur_sum += val
        max_sum = max(cur_sum, max_sum)
    return max_sum


arr = [-1, 2, 3, 4, -4, 5, 6, 7]
print(max_subarray(arr))
