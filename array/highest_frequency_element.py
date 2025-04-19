from collections import Counter


def solve(arr):
    freq = Counter(arr)
    return max(freq, key=freq.get)


a = [2, 3, 2, 34, 5, 2, 3, 3, 3]
print(solve(a))
