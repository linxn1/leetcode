from collections import deque
from typing import List


# 利用 chr(ord()+1)实现

class Solution:
    def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
        rows, cols = len(grid), len(grid[0])
        list1 = []  # 记录开始

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == target[0]:
                    list1.append((r, c))

        def bfs(r, c, index):
            if index == len(target) + 1:
                return True

            for i in range()

            return True

    result = False
    for r, c in list1:
        result = bfs(r, c, 0)
    return result


grid = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
target = "ABCCED"
print(Solution().wordPuzzle(grid, target))
