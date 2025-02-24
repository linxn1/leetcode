from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]

        # 边界
        dp[0][0] = 1
        for r in range(1, rows):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r - 1][0]

        for c in range(1, cols):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c - 1]

        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        # print(dp)
        return dp[rows - 1][cols - 1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0]]))
