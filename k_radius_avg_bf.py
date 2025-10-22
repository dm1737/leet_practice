class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # do sliding window instead
        avgs = []
        for i in range(len(nums)):
            if i < k or i + k > len(nums)-1:
                avgs.append(-1)
            else:
                left = i - k
                total = 0
                while left <= i + k:
                    total += nums[left]
                    left += 1
                avgs.append(total//((k * 2) + 1))
        return avgs
        