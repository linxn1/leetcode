from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def back_track(path, left, right):
            if len(path) == n * 2:
                result.append(''.join(path))
                return
            if left < n:  # 还可以添加左括号
                path.append('(')
                back_track(path, left + 1, right)
                path.pop()
            if right < left:  # 只在左括号多于右括号时添加右括号
                path.append(')')
                back_track(path, left, right + 1)
                path.pop()

        result = []
        back_track([], 0, 0)  # 初始状态，左括号和右括号都是 0
        return result


print(Solution().generateParenthesis(3))
