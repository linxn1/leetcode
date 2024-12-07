from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0, len(prices) - 1):
            profit += max(prices[i + 1] - prices[i], 0)
        return profit


nums = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(nums))
print(nums)
