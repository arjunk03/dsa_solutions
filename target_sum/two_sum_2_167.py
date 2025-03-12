def solution(arr, target):
    st = 0
    end = len(arr) - 1

    while st <= end:
        if arr[st] + arr[end] == target:
            return [st + 1, end + 1]
        elif arr[st] + arr[end] > target:
            end -= 1
        else:
            st += 1

    return -1


a = [2, 7, 11, 15]
print(solution(a, 9))

a = [2, 3, 4]
print(solution(a, 6))

a = [-1, 0]
print(solution(a, -1))

a = [2, 5, 7]
print(solution(a, 8))
