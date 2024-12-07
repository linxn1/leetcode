from collections import deque
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        #  先对数组的进行排序（按照第一个来）
        nums = sorted(intervals, key=lambda x: x[0])
        n = len(nums)
        res.append(nums[0])
        for i in range(1, n):
            if res[-1][1] < nums[i][0]:  # 列表前面的最右端的小于当前区间的最左端，直接将当前区间加入到结果中
                res.append(nums[i])
            else:  # 对应上面的第二种情况
                a, b = res.pop()
                res.append([a, max(b, nums[i][1])])
        return res



intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))
