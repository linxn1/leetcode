class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hp = 0
        while hp <= len(haystack) - len(needle):
            if haystack[hp:hp + len(needle)] == needle:
                return hp
            else:
                hp += 1

        return -1


haystack = "a"
needle = "a"
print(Solution().strStr(haystack, needle))
