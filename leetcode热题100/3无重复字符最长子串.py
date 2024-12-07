class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if s == '':
            return 0

        current_length = 1
        max_length = 1
        for i in range(len(s) - 1):
            for j in range(1, len(s)):
                slice_string = s[i:j + 1]
                if len(slice_string) == len(set(slice_string)):
                    current_length = j - i + 1
                    max_length = max(current_length, max_length)
        return max_length


s = "aa"
print(Solution().lengthOfLongestSubstring(s))
