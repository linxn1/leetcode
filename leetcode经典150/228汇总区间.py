from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        li = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[i] + j - i:
                j += 1
            li.append(str(nums[i]) if i == j - 1 else str(nums[i]) + '->' + str(nums[j - 1]))
            i = j
        return li