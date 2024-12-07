from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        max_num = max(nums)
        for i in range(0, n - 1):
            for j in range(i, n):
                current = 1
                for k in range(i, j + 1):
                    current *= nums[k]
                max_num = max(current, max_num)
        return max_num


nums = [0, 2]
print(Solution().maxProduct(nums))
