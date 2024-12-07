from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left_p = 0
        right_p = len(nums) - 1
        while left_p <= right_p:
            if nums[left_p] == val:
                # 如果left_p指向val，且与right_p指向的不同，则交换
                if nums[right_p] != val:
                    nums[left_p], nums[right_p] = nums[right_p], nums[left_p]
                    left_p += 1  # 移动left_p到新的位置
                right_p -= 1  # 无论是否交换，都减少right_p
            else:
                left_p += 1  # 如果left_p指向的不是val，则移动到下一个位置

        # 由于left_p是在找到非val元素时递增的，因此left_p就是新数组的长度
        return left_p


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = Solution().removeElement(nums, val)
print(nums)
# print(k)
