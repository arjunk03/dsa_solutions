def sumOfSeries(n):
    # code here
    if n <= 1:
        return 1
    return n * n * n + sumOfSeries(n - 1)


a = 5
print(sumOfSeries(a))
