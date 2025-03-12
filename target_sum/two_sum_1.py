def check_sum(arr, target):
    dct = {}

    for val in arr:
        if target - val in dct:
            return True

        dct[val] = True

    return False


arr = [1, 2, 3, 4, 5, 6, 7]
target = 9
print(check_sum(arr, target))

arr = [1, 2, 3, 4, 5, 6, 7]
target = 55
print(check_sum(arr, target))
