def solution(arr):
    if sum(arr) % 3 != 0:
        return False

    if len(arr) < 3:
        return False

    target = sum(arr) // 3
    cur_sum = 0
    part = 0
    for val in arr:
        cur_sum += val

        if cur_sum == target:
            part += 1
            cur_sum = 0

        if part == 3:
            return True

    return False


arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
print(solution(arr))

arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
print(solution(arr))
