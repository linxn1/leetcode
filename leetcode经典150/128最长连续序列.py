from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        new_num = list(set(nums))
        new_num.sort()
        if len(new_num) == 1:
            return 1
        result = [1]
        length = 1

        for i in range(1, len(new_num)):
            if new_num[i] - new_num[i - 1] == 1:
                length += 1
                result.append(length)
            else:
                length = 1
        # print(result)
        return max(result)


print(Solution().longestConsecutive([-6, -1, -1, 9, -8, -6, -6, 4, 4, -3, -8, -1]))
