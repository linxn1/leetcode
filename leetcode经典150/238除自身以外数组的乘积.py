from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        back = 1
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(pre)
            else:
                pre *= nums[i - 1]
                ans.append(pre)
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                ans[i] *= back
            else:
                back *= nums[i + 1]
                ans[i] *= back
        return ans


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
