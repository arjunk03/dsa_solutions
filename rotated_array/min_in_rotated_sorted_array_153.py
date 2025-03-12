def solution(arr):
    st = 0
    end = len(arr) - 1

    while st < end:
        mid = st + (end - st) // 2

        if arr[mid] > arr[end]:
            st = mid + 1
        else:
            end = mid

    return arr[st]


a = [5, 1, 2, 3, 4]
print(solution(a))

a = [5, 1, 2, 3, 4]
print(solution(a))


a = [8, 9, 10, 3, 4, 6, 7]
print(solution(a))


a = [9, 5]
print(solution(a))


a = [5]
print(solution(a))
