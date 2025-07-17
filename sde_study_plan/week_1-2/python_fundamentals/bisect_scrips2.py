import bisect

data = [1, 3, 5, 9]
bisect.insort_left(data, 7)
print(data)

from typing import List

def find_insert_position(nums: List[int], target: int) -> int:
    return bisect.bisect_left(nums, target)

nums = [1, 3, 5, 6]
print(find_insert_position(nums, 5))  # Output: 2 (target already exists)
print(find_insert_position(nums, 2))  # Output: 1 (should go between 1 and 3)
print(find_insert_position(nums, 7))  # Output: 4 (should go at the end)
print(find_insert_position(nums, 0))  # Output: 0 (should go at the start)
