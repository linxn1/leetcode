from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        fast_point = 0
        low_point = 0
        while fast_point < len(nums):
            if nums[fast_point] == nums[low_point]:
                fast_point += 1
                if fast_point - low_point > len(nums) / 2:
                    return nums[low_point]
            else:
                low_point = fast_point


nums = [3, 2, 3]
print(Solution().majorityElement(nums))
