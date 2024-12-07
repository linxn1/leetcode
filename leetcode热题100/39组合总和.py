from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path):
            # 最终递归的条件
            if sum(path) > target:
                return
            elif sum(path) == target:
                for i in result:
                    if set(path) == set(i):
                        return
                result.append(path[:])  # 注意是列表的拷贝
                return

            # 每一次递归,从start_index遍历到n
            for i in range(len(candidates)):
                path.append(candidates[i])
                # print(path[:])
                backtrack(path)
                path.pop()

        result = []  # 最终返回的二维数组
        backtrack(path=[])  # 初始状态.start_index=1.path为空
        return result


print(Solution().combinationSum([2, 3, 6, 7], 7))
