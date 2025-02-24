from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = 0
        for i in range(1, len(prices)):
            num = max(num, prices[i] - min(prices[:i]))
            # print(num)
        return num


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
