from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numlist = nums
        numlist.sort()
        if len(nums) < 3:
            return []

        ans = []
        for i in range(len(numlist) - 2):
            for j in range(i + 1, len(numlist) - 1):
                for k in range(j + 1, len(numlist)):
                    if numlist[i] + numlist[j] + numlist[k] == 0:
                        ans.append((numlist[i], numlist[j], numlist[k]))
        ans = list(set(ans))
        for i in range(len(ans)):
            ans[i] = list(ans[i])

        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
