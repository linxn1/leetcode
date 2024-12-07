from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins == []:
            return -1

        # 初始状态
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        if dp[amount] == float('inf'):



















            return -1
        return dp[amount]


coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))
