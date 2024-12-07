from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast_point = 0
        mid_point = 0
        low_point = 0
        while fast_point < len(nums):
            if nums[fast_point] == nums[mid_point]:
                fast_point += 1
            else:
                mid_point = fast_point
                low_point += 1
                nums[low_point] = nums[fast_point]
        return low_point + 1
