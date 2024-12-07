from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start_index, path):
            if len(path) >= 0:
                result.append(path[:])

            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtrack(start_index=i + 1, path=path)
                path.pop()

        result = []
        backtrack(0, [])
        return result


print(Solution().subsets([1, 2, 3]))
