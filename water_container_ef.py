from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        c_height = min(height[left], height[right])
        max_area = c_height * right
        while left != right:
            if height[left] > height[right]:
                if height[right] > c_height:
                    area = height[right] * (right - left)
                    max_area = max(max_area, area)
                right -= 1
            else:
                if height[left] > c_height:
                    area = height[left] * (right - left)
                    max_area = max(max_area, area)
                left += 1
        return max_area

# The function maxArea calculates the maximum area of water that can be contained between two vertical lines represented by the input list height.
# It uses a two-pointer approach, initializing one pointer at the start (left) and the other at the end (right) of the list.
# The current height (c_height) is determined by the shorter of the two lines at the left and right pointers, and the initial maximum area (max_area) is calculated based on this height and the distance between the two pointers.
# The function enters a loop that continues until the left and right pointers meet. Inside the loop, it compares the heights at the left and right pointers.
# If the height at the left pointer is greater than that at the right pointer, it checks if the height at the right pointer is greater than the current height (c_height). If so, it calculates the area using the height at the right pointer and updates max_area if this area is larger.
# The right pointer is then moved one step to the left.
# If the height at the left pointer is less than or equal to that at the right pointer, it performs a similar check and calculation for the left pointer, moving the left pointer one step to the right afterward.
# This process continues, effectively narrowing the search space while always considering the potential for a larger area.
# Finally, the function returns the maximum area found during the iterations.