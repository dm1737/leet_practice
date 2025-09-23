from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            second = first + 1
            while second <= (len(nums)-1):
                total = nums[first] + nums[second]
                if total == target:
                    val1 = first
                    val2 = second
                    return [val1, val2]
                else:
                    second += 1
        return []

# The function twoSum takes a list of integers (nums) and a target integer (target) as input and returns the indices of the two numbers that add up to the target.
# The algorithm follows these steps:
# 1. Iterate through the list with a for loop using the variable 'first' to represent the index of the first number.
# 2. For each 'first' index, initialize a 'second' index to be one position ahead.
# 3. Use a while loop to check pairs of numbers by summing the values at 'first' and 'second' indices.
# 4. If the sum equals the target, return the indices as a tuple.
# 5. If no pair is found by the end of the loops, return an empty list.
