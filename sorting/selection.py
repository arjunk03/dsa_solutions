def sorting(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            print(i, j, len(arr))
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]
    return arr


a = [3, 5, 2, 1, 55, 6, 3]
print(sorting(a))
