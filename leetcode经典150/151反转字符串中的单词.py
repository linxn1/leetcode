class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        if len(strs) <= 1:
            new_string = ''
            for i in strs:
                new_string += i
            return new_string
        new_string = ''
        for i in reversed(strs):
            new_string += i + r' '
        return new_string[:-1]


s = "the sky is blue"
print(Solution().reverseWords(s))
