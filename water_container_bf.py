from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            j = len(height)
            while j < len(height):
                width = j - i
                l_height = min(height[i], height[j])
                area = width * l_height
                max_area = max(max_area, area)
                j += 1
        return max_area

# The function maxArea calculates the maximum area of water that can be contained between two vertical lines represented by the input list height.
# It uses a brute-force approach by iterating through all possible pairs of lines using two nested loops.
# The outer loop iterates through each line using the index i, while the inner loop iterates through the lines to the right of i using the index j.
# For each pair of lines (i, j), the function calculates the width as the difference between the indices j and i.
# It then determines the limiting height (l_height) as the minimum of the two heights at indices i and j.
# The area is calculated by multiplying the width by the limiting height.   
# The function keeps track of the maximum area found during the iterations by comparing the current area with the previously recorded maximum area (max_area).
# Finally, the function returns the maximum area found after all pairs of lines have been evaluated.