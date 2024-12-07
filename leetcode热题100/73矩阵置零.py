from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i_list = []
        j_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    i_list.append(i)
                    j_list.append(j)
        i_list = list(set(i_list))
        j_list = list(set(j_list))
        for i in i_list:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in j_list:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        print(matrix)


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(Solution().setZeroes(matrix))
