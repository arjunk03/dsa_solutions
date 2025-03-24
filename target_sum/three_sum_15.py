def solution(arr, target):
    arr.sort()
    res = set()
    for i, val in enumerate(arr):
        start = i + 1
        end = len(arr) - 1

        while start < end:
            if arr[start] + arr[end] + arr[i] == target:
                res.add((arr[start], arr[end], arr[i]))
                start += 1
                end -= 1
            elif arr[start] + arr[end] + arr[i] > target:
                end = end - 1
            else:
                start = start + 1
    return list(res)


arr = [-1, 0, 1, 2, -1, -4]
print(solution(arr, 0))
