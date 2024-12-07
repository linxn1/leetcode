class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))
