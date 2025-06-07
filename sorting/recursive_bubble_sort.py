def sorting_bubble(arr, i, k):
    if i == k:
        return arr

    for j in range(k):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return sorting_bubble(arr, i + 1, k)


a = [22, 44, 78, 88, 9]
print(sorting_bubble(a))
