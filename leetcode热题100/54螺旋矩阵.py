from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        list1 = []
        while top <= bottom and left <= right:
            if top<=bottom:
                for i in range(left, right + 1):
                    list1.append(matrix[top][i])
                top += 1
            if left <= right:
                for i in range(top, bottom + 1):
                    list1.append(matrix[i][right])
                right -= 1
            if top <= bottom:
                for i in reversed(range(left, right + 1)):
                    list1.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in reversed(range(top, bottom + 1)):
                    list1.append(matrix[i][left])
                left += 1
        return list1


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spiralOrder(matrix))
