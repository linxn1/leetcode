from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums1 = []
        for i in nums:
            if i != 0:
                nums1.append(i)
        for i in range(len(nums)):
            if i < len(nums1):
                nums[i] = nums1[i]
            else:
                nums[i] = 0


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
print(nums)
