from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid[0])
        col = len(grid)
        dp = [[0 for _ in range(row)] for _ in range(col)]

        dp[0][0] = grid[0][0]

        for i in range(1, row):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
        for j in range(1, col):
            dp[j][0] = grid[j][0] + dp[j - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                dp[j][i] = min(dp[j - 1][i], dp[j][i - 1]) + grid[j][i]
        return dp[col - 1][row - 1]


grid = [[1, 2, 3], [4, 5, 6]]
print(Solution().minPathSum(grid))
