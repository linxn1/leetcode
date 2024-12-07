from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        sum_list = []
        for i in range(n):
            sum_list.append(sum(nums[:i + 1]))
        # print(sum_list)

        dp = [0] * n
        dp[0] = sum_list[0]
        for i in range(1, n):
            dp[i] = sum_list[i] - min(min(sum_list[:i]), 0)
        # print(dp)
        return max(dp)


nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums))
