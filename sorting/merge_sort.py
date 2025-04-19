class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1

        print(temp)
        for i in range(low, high + 1):
            print(len(temp), i, low, high)
            arr[i] = temp[i - low]

        return temp

    def merge_sort_array(self, nums, low, high):
        if low >= high:
            return

        mid = low + (high - low) // 2

        self.merge_sort_array(nums, low, mid)
        self.merge_sort_array(nums, mid + 1, high)
        new = self.merge(nums, low, mid, high)
        return new

    def mergeSort(self, nums):
        return self.merge_sort_array(nums, 0, len(nums) - 1)


sol = Solution()
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(sol.mergeSort(arr))
