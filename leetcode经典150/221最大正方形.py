from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 or n == 1:
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == '1':
                        return 1
            return 0
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        max_num = 0
        for i in range(m):
            for j in range(n):
                max_num = max(max_num, dp[i][j])
        return max_num * max_num


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
print(Solution().maximalSquare(matrix))
