from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals += [newInterval]

        intervals.sort(key=lambda x: x[0])
        # print(intervals)

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            current = result[-1]
            if current[1] < intervals[i][0]:
                result.append(intervals[i])
                continue
            if current[1] >= intervals[i][0]:
                result[-1][1] = max(current + intervals[i])
        return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

print(Solution().insert(intervals, newInterval))
