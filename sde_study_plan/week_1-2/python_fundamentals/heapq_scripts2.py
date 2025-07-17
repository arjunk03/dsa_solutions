import heapq

data = [10, 5, 20, 15, 25]
heapq.heapify(data)
print(data)
res = heapq.nlargest(3, data)
print(res)

heapq.