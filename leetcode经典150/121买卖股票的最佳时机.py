from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit_temp = prices[i] - min(prices[0:i])
            profit = max(profit_temp, profit)
        return profit


nums = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(nums))
print(nums)
