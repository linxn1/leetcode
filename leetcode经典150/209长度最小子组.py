from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

            # 初始化左指针、右指针、当前和、最小长度（初始化为一个较大的数）
        left = 0
        right = 0
        current_sum = 0
        min_length = float('inf')

        # 遍历数组
        while right < len(nums):
            # 扩大窗口
            current_sum += nums[right]
            # 当当前和大于或等于目标值时
            while current_sum >= target:
                # 更新最小长度
                min_length = min(min_length, right - left + 1)
                # 缩小窗口
                current_sum -= nums[left]
                left += 1
            right += 1

            # 如果没有找到满足条件的子数组，则返回0
        if min_length == float('inf'):
            return 0
        return min_length


print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
