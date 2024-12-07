class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]

        nums1.sort()
        # print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(Solution().merge(nums1, m, nums2, n))
