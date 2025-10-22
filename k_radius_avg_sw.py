class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if k == 0:
            return nums            
        
        avgs = [-1] * len(nums)
        n = len(nums)
        
        window_size = (k * 2) + 1
        
        if window_size > n:
            return avgs
        
        window_sum = sum(nums[:window_size])
        avgs[k] = window_sum // window_size
        
        for i in range(window_size, n):
            window_sum = window_sum - nums[i - window_size] + nums[i]
            avgs[i - k] = window_sum // window_size
        
        return avgs