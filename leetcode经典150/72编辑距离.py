class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # +1 是为了包含空字符串的情况，但这里其实不需要，因为我们在循环中不用到dp[m][n]

        # 初始化第一行和第一列
        for i in range(m + 1):
            dp[i][0] = i  # word1的前i个字符转换为空字符串需要i次删除
        for j in range(n + 1):
            dp[0][j] = j  # word2的前j个字符转换为空字符串需要j次删除

        # 填充dp数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 字符相同，不需要操作，继承之前的最小编辑距离
                else:
                    dp[i][j] = min(dp[i - 1][j],  # 删除word1[i-1]
                                   dp[i][j - 1],  # 插入word2[j-1]
                                   dp[i - 1][j - 1]) + 1  # 替换word1[i-1]为word2[j-1]

        return dp[m][n]