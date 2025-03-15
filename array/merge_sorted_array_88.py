def solution(arr1, arr2, m, n):
    p1 = m - 1
    p2 = n - 1
    i = m + n - 1

    while p2 >= 0:
        # print(arr1, arr2, p1, p2, i)
        if p1 >= 0 and arr1[p1] >= arr2[p2]:
            arr1[i] = arr1[p1]
            p1 -= 1
        else:
            arr1[i] = arr2[p2]
            p2 -= 1
        i -= 1

    return arr1


#
# arr1 = [1, 3, 5, 0, 0, 0]
# arr2 = [2, 4, 6]
# print(solution(arr1, arr2, 3, 3))
#
# arr1 = [1, 3, 5, 0, 0, 0]
# arr2 = [2, 3, 6]
# print(solution(arr1, arr2, 3, 3))
#
# arr1 = [1, 2, 5, 0, 0, 0]
# arr2 = [2, 4, 6]
# print(solution(arr1, arr2, 3, 3))
#
# arr1 = [1, 3, 5, 7, 8, 0, 0, 0]
# arr2 = [2, 4, 6]
# print(solution(arr1, arr2, 5, 3))

arr1 = [0]
arr2 = [2]
print(solution(arr1, arr2, 0, 1))
