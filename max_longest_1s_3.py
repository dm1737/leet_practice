class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = curr = zeros = max1 = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            curr = right - left + 1
            max1 = max(max1, curr)
            
        return max1
        