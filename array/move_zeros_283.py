def solution(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1


arr = [1, 2, 0, 5, 6, 0, 8, 9]
solution(arr)
print(arr)

arr = [0]
solution(arr)
print(arr)
