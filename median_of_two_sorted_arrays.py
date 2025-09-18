from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 0:
            middle = length//2
            median = (nums[middle] + nums[(middle-1)])/2
        else: 
            target = ((length + 1)//2)-1
            median = nums[target]

        return median

# The function find_median_sorted_arrays takes two sorted arrays (nums1 and nums2) as input and returns the median of the combined sorted array.
# The algorithm follows these steps:
# 1. Merge the two arrays into one sorted array.
# 2. Find the length of the merged array.
# 3. If the length is odd, return the middle element.
# 4. If the length is even, return the average of the two middle elements.