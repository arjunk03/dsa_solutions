def product(arr):
    prefix = 1
    postfix = 1

    res = [1] * len(arr)

    for i in range(len(arr)):
        if i == 0:
            p_val = 1
        else:
            p_val = arr[i - 1]

        new_val = p_val * prefix
        prefix = new_val
        res[i] = new_val

    for j in range(len(arr) - 1, -1, -1):
        if j == len(arr) - 1:
            p_val = 1
        else:
            p_val = arr[j + 1]
        new_val = p_val * postfix
        postfix = new_val
        res[j] = new_val * res[j]

    return res


arr = [1, 2, 3, 4]
print(product(arr))
