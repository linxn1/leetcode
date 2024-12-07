from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        # 行
        for r in range(rows):
            current_list = []
            for c in range(cols):
                if board[r][c] != '.':
                    current_list.append(board[r][c])
                if len(current_list) != len(set(current_list)):
                    return False

        # 列
        for c in range(cols):
            current_list = []
            for r in range(rows):
                if board[r][c] != '.':
                    current_list.append(board[r][c])
                if len(current_list) != len(set(current_list)):
                    return False

        list1 = [0, 3, 6]
        for num1 in list1:
            for num2 in list1:
                current_list = []
                print(num1,num2)
                for r in range(num1, num1 + 3):
                    for c in range(num2, num2 + 3):
                        if board[r][c] != '.':
                            current_list.append(board[r][c])
                        if len(current_list) != len(set(current_list)):
                            return False

        return True


board = [[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]

for i in board:
    for j in i:
        print(j, end='|')
    print()
print(Solution().isValidSudoku(board))
