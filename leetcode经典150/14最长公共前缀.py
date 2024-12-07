from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = strs[0]
        for item in strs:
            while not item.startswith(string):
                if len(string) == 0:
                    return ''
                string = string[:-1]

        return string


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
