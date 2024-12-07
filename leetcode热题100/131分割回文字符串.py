from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start, path):
            if len(path) == 2:
                result.append(path[:])
                return
            for i in range(start, len(s)):
                path.append(s[i])
                if start + 1 - i == 1:
                    backtrack(start + 1, path)
                path.pop()

        result = []
        backtrack(0, [])
        print(result)


s = 'aab'
print(Solution().partition(s))
