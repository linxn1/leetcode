from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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


intervals = [[1, 4], [0, 4]]
print(Solution().merge(intervals))
