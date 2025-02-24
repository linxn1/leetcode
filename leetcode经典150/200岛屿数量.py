from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        # 定义四个方向，向上、向下、向左、向右
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'  # 将陆地标记为水域

            while queue:
                curr_r, curr_c = queue.popleft()

                # 遍历四个方向
                for dr, dc in directions:
                    new_r, new_c = curr_r + dr, curr_c + dc

                    # 检查边界和水域
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1':
                        grid[new_r][new_c] = '0'  # 将新陆地标记为水域
                        queue.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # 找到一个新岛屿
                    num_islands += 1
                    bfs(r, c)  # 从该岛屿开始 BFS

        return num_islands


# 示例测试
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(Solution().numIslands(grid1))  # 输出：1
print(Solution().numIslands(grid2))  # 输出：3


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rols, cols = len(grid), len(grid[0])
        num_islands = 0

        # 定义四个方向
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            # 标记为水域
            grid[r][c] = '0'

            while queue:
                rb, cb = queue.popleft()
                for xb, yb in directions:
                    x, y = rb + xb, cb + yb
                    if 0 <= x < rols and 0 <= y < cols and grid[x][y] == '1':
                        grid[x][y] = '0'
                        queue.append((x, y))

        for r in range(rols):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    bfs(r, c)
        print(grid)
        return num_islands


# 示例测试
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(Solution().numIslands(grid1))
print(Solution().numIslands(grid2))
