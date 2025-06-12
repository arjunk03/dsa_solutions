a = [1, 2, 3, 4, 5, 6]

res = [val for val in a if val % 2 == 0]

print(res)


a = ["apple", "banana", "cherry"]

res = {val: len(val) for val in a}

print(res)

res = [val * val for val in range(4)]
print(res)


def filter_and_transform(data):
    res = [val for val in data if val["age"] > 18]
    return res


a = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 17},
    {"name": "Bob", "age": 30},
]
res = filter_and_transform(a)
print(res)

a = "test the data with"
res = {char.lower() for char in a}
print(res)

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8, 10]
res = [val for val in a if val in b]
print(res)

a = [[2, 3, 4], [44, 56, 67], [4, 5, 6]]
res = [val for v in a for val in v]
print(res)


sum_sq = sum(val * val for val in range(1, 101))
print(sum_sq)
