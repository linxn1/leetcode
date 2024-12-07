from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        dp = []
        for i in range(len(triangle)):
            dp.append([0 for _ in range(i + 1)])
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            dp[i][0] = triangle[i][0] + dp[i - 1][0]
        for j in range(1, len(triangle)):
            dp[j][j] = dp[j - 1][j - 1] + triangle[j][j]

        for i in range(1, len(dp)):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
