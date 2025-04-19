def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


a = [23, 44, 66, 22, 11, 4, 4, 3, 2, 1]
print(bubble(a))


def bubble2(arr):
    swap = False
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

        if not swap:
            break
        print("nnn")

    return arr


a = [23, 44, 66, 22, 11, 4, 4, 3, 2, 1]
print(bubble2(a))

a = [1, 2, 3, 4, 5, 6, 7]
print(bubble2(a))
