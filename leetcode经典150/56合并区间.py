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


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            # 如果当前区间与上一个区间有重叠
            if intervals[i][0] <= result[-1][1]:
                # 合并两个区间，更新结束时间为较大值
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                # 否则直接将当前区间添加到结果中
                result.append(intervals[i])
        return result


intervals = [[1, 4], [0, 4], [5, 6]]
print(Solution().merge(intervals))
