def check_duplicate(arr, k):
    dct = {}

    for i, val in enumerate(arr):
        if val in dct and (i - dct[val]) <= k:
            return True

        dct[val] = i

    return False


a = [1, 2, 3, 4, 5, 6, 1]
print(check_duplicate(a, 3))


a = [1, 2, 3, 2, 5, 6, 1]
print(check_duplicate(a, 3))
