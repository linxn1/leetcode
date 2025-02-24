class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 边界条件检查
        if len(s1) + len(s2) != len(s3):
            return False

            # 初始化动态规划数组
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 初始化第一行（当 s1 为空字符串，只考虑 s2 的情况）
        for j in range(n + 1):
            if j == 0 or (j > 0 and s2[:j] == s3[:j] and (j == 1 or dp[0][j - 1])):
                dp[0][j] = True

                # 初始化第一列（当 s2 为空字符串，只考虑 s1 的情况）
        for i in range(m + 1):
            if i == 0 or (i > 0 and s1[:i] == s3[:i] and (i == 1 or dp[i - 1][0])):
                dp[i][0] = True

                # 填充动态规划数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 检查是否可以从 dp[i-1][j]（使用 s1 的字符）或 dp[i][j-1]（使用 s2 的字符）转移而来
                if (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]):
                    dp[i][j] = True

                    # 返回结果（s1 和 s2 是否可以交错组成 s3）
        return dp[m][n]

    # 测试


solution = Solution()
print(solution.isInterleave("aabc", "dbbca", "aadbbcbcac"))  # 输出: True
print(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # 输出: False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # 初始化动态规划数组
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for dm in range(1, m + 1):
            if s1[:dm] == s3[:dm]:
                dp[dm][0] = True
        for dn in range(1, n + 1):
            if s2[:dn] == s3[:dn]:
                dp[0][dn] = True

        for dm in range(1, m + 1):
            for dn in range(1, n + 1):
                if (s1[dm - 1] == s3[dm + dn - 1] and dp[dm - 1][dn]) or (
                        s2[dn - 1] == s3[dm + dn - 1] and dp[dm][dn - 1]):
                    dp[dm][dn] = True

        # print(dp)
        return dp[m][n]


solution = Solution()
print(solution.isInterleave("aac", "bc", "aabcc"))  # 输出: True
print(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # 输出: False
