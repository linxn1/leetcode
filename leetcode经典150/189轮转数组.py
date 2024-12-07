from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        # 0-k
        slice1 = nums[0:len(nums) - k]
        slice2 = nums[len(nums) - k:len(nums)]

        nums[k:len(nums)] = slice1
        nums[0:k] = slice2
        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
print(Solution().rotate(nums, 3))
