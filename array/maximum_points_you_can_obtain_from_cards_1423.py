def solution(arr, k):
    nums = cardPoints
    l, r = 0, len(nums) - k
    total = sum(nums[r:])
    ans = total

    while r < len(nums):
        total += nums[l] - nums[r]
        l += 1
        r += 1
        ans = max(ans, total)

    return ans


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(solution(cardPoints, k))


cardPoints = [2, 2, 2]
k = 2
print(solution(cardPoints, k))
