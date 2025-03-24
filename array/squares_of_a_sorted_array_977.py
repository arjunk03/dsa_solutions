def solution(nums):
    start = 0
    end = len(nums) - 1
    result = [0] * len(nums)
    index = len(nums) - 1

    while start <= end:
        if abs(nums[start]) > abs(nums[end]):
            result[index] = nums[start] * nums[start]
            start += 1
        else:
            result[index] = nums[end] * nums[end]
            end -= 1
        index -= 1

    return result


arr = [-4, -1, 0, 3, 10]
print(solution(arr))
