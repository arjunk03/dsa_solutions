import heapq
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 2)
print(heap) # Output might be [1, 2, 7, 4] (order of other elements is not strictly sorted, only the heap property is maintained)


smallest = heapq.heappop(heap)
print(smallest) # Output: 1
print(heap)     # Output: [2, 4, 7] (again, order of others is not strictly sorted)

data = [5, 1, 9, 3, 7, 2]
heapq.heapify(data)
print(data) # Output: [1, 2, 3, 5, 7, 9] (smallest is at 0, others maintain heap property)


heap = [1, 2, 7, 4]
# Push 0, then pop smallest (which will be 0)
returned_val = heapq.heappushpop(heap, 0)
print(returned_val) # Output: 0
print(heap)         # Output: [1, 2, 7, 4] (the original 1 is now smallest)

heap = [1, 2, 7, 4]
# Replace 1 with 10. Returns 1. Heap now contains 2,4,7,10 (in heap order)
returned_val = heapq.heapreplace(heap, 0)
print(returned_val) # Output: 1
print(heap)         # Output: [2, 4, 7, 10] (after re-heapifying)



data = [10, 4, 8, 2, 12, 6]
largest_3 = heapq.nlargest(3, data)
smallest_2 = heapq.nsmallest(2, data)
print(largest_3)  # Output: [12, 10, 8]
print(smallest_2) # Output: [2, 4]

list1 = [1, 5, 9]
list2 = [2, 6, 10]
list3 = [3, 7, 11]
merged_list = list(heapq.merge(list1, list2, list3))
print(merged_list) # Output: [1, 2, 3, 5, 6, 7, 9, 10, 11]