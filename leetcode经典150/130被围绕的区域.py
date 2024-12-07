from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        # 计算从边缘向中心扩散
        queue = deque()
        # 初始队列
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows - 1] or c in [0, cols - 1]) and board[r][c] == 'O':
                    queue.append((r, c))

        # print(queue)

        def bfs(r, c):
            board[r][c] = '#'
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            # r, c = queue.popleft()
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                        board[nr][nc] = '#'
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows - 1] or c in [0, cols - 1]) and board[r][c] == 'O':
                    bfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        return board


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
print(Solution().solve(board))
