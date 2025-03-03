# soluion 1
def check_duplicate(arr):
    arr.sort()

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False


a = [1, 2, 3, 4, 5, 61, 1]
print(check_duplicate(a))

a = [1, 2, 3, 4, 5, 61]
print(check_duplicate(a))


# solution 2
def check_duplicate_2(arr):
    return len(arr) != len(set(arr))


a = [1, 2, 3, 4, 5, 61, 1]
print(check_duplicate_2(a))

a = [1, 2, 3, 4, 5, 61]
print(check_duplicate_2(a))
