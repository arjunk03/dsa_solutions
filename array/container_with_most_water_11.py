
# Brute force solution to find the maximum area of water that can be contained
def most_water(arr):
    max_area = 0
    indexs = []
    
    if len(arr) < 2:
        return None
    
    # p1 = 0
    # while p1 < len(arr) - 1:
    #     p2 = p1 + 1
    #     while p2 < len(arr):
    #         area = min(arr[p1], arr[p2]) * (p2 - p1)
    #         if area > max_area:
    #             indexs = [p1, p2]
    #             max_area = area

    #         p2 += 1
    #     p1 += 1

    # for p1, val in enumerate(arr):
    #     p2 = p1 + 1
    #     while p2 < len(arr):
    #         area = min(val, arr[p2]) * (p2 - p1)
    #         if area > max_area:
    #             indexs = [p1, p2]
    #             max_area = area
    #         p2 += 1

    # return indexs

    for p1, val in enumerate(arr):
        p2 = p1 + 1
        while p2 < len(arr):
            area = min(val, arr[p2]) * (p2 - p1)
            max_area = max(area, max_area)
            p2 += 1

    return max_area

# a = [7,1,2,9, 3]
# res = most_water(a)
# print(res)


# a = [7,1]
# res = most_water(a)
# print(res)


# a = []
# res = most_water(a)
# print(res)


# a = [7,1, 2, 4, 6]
# res = most_water(a)
# print(res)


# optimal solution
def most_water(arr):
    max_area = 0
    left = 0
    right = len(arr) - 1

    while left < right:
         area = min(arr[left], arr[right]) * (right - left)
         max_area = max(area, max_area)
         if arr[left] < arr[right]:
             left += 1
         else:
             right -= 1

    return max_area


a = [7,1,2,9, 3]
res = most_water(a)
print(res)


a = [7,1]
res = most_water(a)
print(res)


a = []
res = most_water(a)
print(res)


a = [7,1, 2, 4, 6]
res = most_water(a)
print(res)


