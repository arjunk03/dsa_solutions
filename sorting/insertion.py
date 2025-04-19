def insertion(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


a = [3, 4, 24, 55, 5, 77, 11, 33]
print(insertion(a))
