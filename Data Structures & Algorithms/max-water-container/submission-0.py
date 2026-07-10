from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            current = min(height[left], height[right]) * width
            max_water = max(max_water, current)

            # Move the shorter bar
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water