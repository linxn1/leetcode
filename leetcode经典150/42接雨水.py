from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        max_index = height.index(max_height)

        current_left_height = 0
        current_right_height = 0
        water_sum = 0
        for i in range(max_index):
            current_left_height = max(current_left_height, height[i])
            water_sum = water_sum + current_left_height - height[i]
        for i in reversed(range(max_index, len(height))):
            current_right_height = max(current_right_height, height[i])
            water_sum = water_sum + current_right_height - height[i]
        return water_sum


height = [4, 2, 0, 3, 2, 5]
print(Solution().trap(height))
