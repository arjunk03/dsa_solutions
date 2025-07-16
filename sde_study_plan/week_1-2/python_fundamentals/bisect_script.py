import bisect

data = [1, 3, 5, 5, 7, 9]

# Find insertion point for 4
idx_4 = bisect.bisect_left(data, 4)
print(f"bisect_left(data, 4): {idx_4}") # Output: 2 (index where 4 should be inserted: [1, 3, *4*, 5, 5, 7, 9])

# Find insertion point for 5 (returns index of the first 5)
idx_5_left = bisect.bisect_left(data, 5)
print(f"bisect_left(data, 5): {idx_5_left}") # Output: 2


# Find insertion point for 4
idx_4 = bisect.bisect_right(data, 4)
print(f"bisect_left(data, 4): {idx_4}") # Output: 2 (index where 4 should be inserted: [1, 3, *4*, 5, 5, 7, 9])

# Find insertion point for 5 (returns index of the first 5)
idx_5_left = bisect.bisect_right(data, 5)
print(f"bisect_left(data, 5): {idx_5_left}") # Output: 2


my_list = [1, 3, 5, 7]
bisect.insort_left(my_list, 4)
print(my_list) # Output: [1, 3, 4, 5, 7]
bisect.insort_left(my_list, 3) # Inserts BEFORE the existing 3
print(my_list) # Output: [1, 3, 3, 4, 5, 7]

my_list = [1, 3, 5, 7]
bisect.insort_right(my_list, 4)
print(my_list) # Output: [1, 3, 4, 5, 7]
bisect.insort_right(my_list, 3) # Inserts AFTER the existing 3
print(my_list) # Output: [1, 3, 3, 4, 5, 7]