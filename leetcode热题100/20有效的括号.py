class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = [0]
        for i in range(len(s)):
            stack.append(s[i])
            if stack[-2:] == ['(', ')'] or stack[-2:] == ['[', ']'] or stack[-2:] == ['{', '}']:
                stack.pop(-1)
                stack.pop(-1)
        if len(stack) == 1:
            return True
        else:
            return False


s = "([])"
Solution().isValid(s)
