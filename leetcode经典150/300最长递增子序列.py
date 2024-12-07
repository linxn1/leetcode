from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # 初始化dp数组
        maxLength = 1  # 最长递增子序列的初始长度为1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 更新dp[i]
            maxLength = max(maxLength, dp[i])  # 更新最长长度

        return maxLength


print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))
