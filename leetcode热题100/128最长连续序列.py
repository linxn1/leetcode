from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        dictlist = {}
        nums.sort()
        print(nums)
        for i in nums:
            if i in dictlist:
                dictlist[i] += 1
            else:
                dictlist[i] = 0
                dictlist[i] += 1

        current_len = 1
        max_len = 1

        if len(dictlist) == 1:
            return 1
        for i in range(1, len(dictlist)):
            if list(dictlist.keys())[i] - list(dictlist.keys())[i - 1] == 1:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
        if max_len == 1:
            return 0
        return max_len


nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(Solution().longestConsecutive(nums))
