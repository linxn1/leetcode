from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            for j in range(int(len(matrix) / 2)):
                matrix[i][j], matrix[i][len(matrix) - j - 1] = matrix[i][len(matrix) - j - 1], matrix[i][j]
        print(matrix)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().rotate(matrix))
