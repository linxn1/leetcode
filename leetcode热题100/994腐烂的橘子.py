from collections import deque
from typing import List


# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         fresh = 0  # 新鲜橘子的数量
#         queue = deque()  # 队列存放腐烂橘子的坐标和时间步
#
#         # 初始化队列并统计新鲜橘子的数量
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 2:  # 腐烂橘子
#                     queue.append((r, c, 0))  # (row, col, time)
#                 elif grid[r][c] == 1:  # 新鲜橘子
#                     fresh += 1
#
#         # 定义四个方向，向上、向下、向左、向右
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         minutes = 0  # 记录时间
#
#         # 开始 BFS 传播腐烂
#         while queue:
#             r, c, minutes = queue.popleft()
#
#             # 尝试将邻居橘子腐烂
#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
#                     grid[nr][nc] = 2  # 让新鲜橘子腐烂
#                     fresh -= 1  # 新鲜橘子数量减少
#                     queue.append((nr, nc, minutes + 1))  # 将新的腐烂橘子加入队列
#
#         # 如果没有剩余新鲜橘子，返回时间步，否则返回 -1
#         return minutes if fresh == 0 else -1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0  # 新鲜橘子个数
        minute = 0  # 时间
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # 开始腐烂
        while queue:
            r, c, time = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    queue.append((nr, nc, time + 1))
                    grid[nr][nc] = 2
                    minute = max(minute, time + 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minute


# 示例测试
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))  # 输出：4
