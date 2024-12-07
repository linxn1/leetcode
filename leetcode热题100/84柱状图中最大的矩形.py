from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        current_area = 0
        max_area = max(heights)
        for i in range(len(heights) - 1):
            for j in range(i, len(heights)):
                current_area = (j - i + 1) * min(heights[i:j + 1])
                max_area = max(current_area, max_area)
        return max_area


heights = [0,9]
print(Solution().largestRectangleArea(heights))
