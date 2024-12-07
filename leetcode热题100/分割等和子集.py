from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return True
            else:
                return False

        for i in range(len(nums)):  # 分割元素个数
            current_sum1 = 0
            current_sum2 = sum(nums)
            for j in range(i):
                current_sum1+=


nums = [1, 5, 11, 5]
print(Solution().canPartition(nums))
