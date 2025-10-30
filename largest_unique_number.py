from collections import List, defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        tracker = defaultdict(int)
        largest = -1
        
        for num in nums:
            tracker[num] += 1
            
        for val in tracker:
            if tracker[val] == 1:
                largest = max(largest, val) 
            
        return largest
