class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list1 = list(pattern)
        list2 = s.split()

        return [list1.index(i) for i in list1]==[list2.index(j) for j in list2]


print(Solution().wordPattern("abba", "dog cat cat dog"))
