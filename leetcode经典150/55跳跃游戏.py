from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        boollist = [False] * len(nums)
        fast_p = 0
        low_p = 0
        while fast_p < len(nums):
            if fast_p + nums[fast_p] > len(nums):
                return True
            else:
                for i in range(nums[fast_p]):
                    boollist[fast_p + i] = True
                fast_p += nums[fast_p]
            if nums[fast_p] == 0

        return False


nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
