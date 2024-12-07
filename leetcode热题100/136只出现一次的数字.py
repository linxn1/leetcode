from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        for i in range(0, len(nums) - 2, 2):
            if nums[i + 1] - nums[i] != 0:
                return nums[i]
        return nums[-1]


nums = [2, 2, 1]
print(Solution().singleNumber(nums))
