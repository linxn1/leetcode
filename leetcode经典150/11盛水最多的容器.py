from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        for i in range(len(height) - 1):
            for j in range(i, len(height)):
                area = (j - i) * min(height[i], height[j])
                maxArea = max(maxArea, area)
        return maxArea


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
