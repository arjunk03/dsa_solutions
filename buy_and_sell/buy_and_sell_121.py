def get_maximum_profit(arr):
    buy = arr[0]
    profit = 0

    for val in arr:
        if val < buy:
            buy = val
        elif val - buy > profit:
            profit = val - buy

    return profit


arr = [7, 1, 5, 6, 4, 2]
print(get_maximum_profit(arr))
