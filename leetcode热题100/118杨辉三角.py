from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        dp = []
        for i in range(numRows):
            dp.append([1] * (i + 1))

        dp[0][0] = dp[1][0] = dp[1][1] = 1
        for i in range(1, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp


print(Solution().generate(5))
