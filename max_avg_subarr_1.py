class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = max_avg = sums = 0
        for val in range(k):
            sums += nums[val]
            max_avg = sums/k
            
        for val in range(k, len(nums)):
            sums += nums[val] - nums[val - k]
            curr = sums/k
            max_avg = max(max_avg, curr)
            
        return max_avg
        