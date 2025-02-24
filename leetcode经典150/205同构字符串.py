class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(i) for i in s] == [t.index(j) for j in t]


print(Solution().isIsomorphic("egg", "add"))
