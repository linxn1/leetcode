class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        s_point = 0
        t_point = 0
        count = 0
        while s_point < len(s) and t_point < len(t):
            if t[t_point] == s[s_point]:
                t_point += 1
                s_point += 1
                count += 1
                if count == len(s):
                    return True
            else:
                t_point += 1
        return False


print(Solution().isSubsequence("abc", "ahbgdc"))
