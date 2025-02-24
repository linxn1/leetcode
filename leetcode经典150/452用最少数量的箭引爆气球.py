from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda a: a[0])
        current = points[0]
        num = 1
        for i in range(len(points)):
            if current[1] < points[i][0]:
                num += 1
                current = points[i]
            if current[1] >= points[i][0]:
                current = [max(current[0], points[i][0]), min(current[1], points[i][1])]
        return num


print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
