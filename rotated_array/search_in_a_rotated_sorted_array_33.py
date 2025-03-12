def solution(arr, target):
    st = 0
    end = len(arr) - 1

    while st <= end:
        mid = st + (end - st) // 2

        if arr[mid] == target:
            return mid
        elif arr[st] <= arr[mid]:
            if arr[st] <= target < arr[mid]:
                end = mid - 1
            else:
                st = mid + 1
        else:
            if arr[mid] < target <= arr[end]:
                st = mid + 1
            else:
                end = mid - 1
    return -1


a = [5, 6, 8, 1, 2, 3]
print(solution(a, 3))

a = [5, 6, 8, 1, 2, 3]
print(solution(a, 8))
