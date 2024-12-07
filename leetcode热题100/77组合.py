from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start_index, path):
            # 最终递归的条件
            if len(path) == k:
                result.append(path[:])  # 注意是列表的拷贝
                return

            # 每一次递归,从start_index遍历到n
            for i in range(start_index, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        result = []  # 最终返回的二维数组
        backtrack(start_index=1, path=[])  # 初始状态.start_index=1.path为空
        return result


print(Solution().combine(100, 41))
