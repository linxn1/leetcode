class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        max1=''
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j]==s[i:j][::-1]:
                    curr=len(s[i:j])
                    max1=s[i:j] if curr>len(max1) else max1
        return max1



print(Solution().longestPalindrome("babad"))