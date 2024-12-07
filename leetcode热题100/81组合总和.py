from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start_index, path):
            if sum(path) == target:  # 退出条件
                result.append(path[:])  # 添加path的拷贝
                return

            # 单次开始
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                # backtrack(start_index=i + 1, path=path) # 不可用无限次被选取,从i+1开始
                backtrack(start_index=0, path=path)  # 可以无限次被选取,从0开始
                path.pop()

        result = []
        backtrack(start_index=0, path=[])
        return result


print(Solution().combinationSum([2, 3, 6, 7], 7))
