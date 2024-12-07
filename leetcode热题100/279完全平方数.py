class Solution:
    def numSquares(self, n: int) -> int:
        length = int(pow(n, 1 / 2)) + 1
        nums = [i * i for i in range(1, length + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n + 1):
            for num in nums:
                if num <= i:
                    dp[i] = min(dp[i - num] + 1, dp[i])
        if dp[n - 1] == float('inf'):
            return -1
        print(dp)
        return dp[n]


print(Solution().numSquares(12))
