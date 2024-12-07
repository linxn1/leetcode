from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def back_track(path):
            if len(path) == len(nums):  # 如果path长度等于nums长度，说明找到了一个全排列
                result.append(path[:])  # 注意要添加path的副本
                return
            for i in range(len(nums)):  # 遍历nums中的所有元素
                if nums[i] in path:  # 如果当前元素已经在path中，跳过
                    continue
                path.append(nums[i])  # 将当前元素加入path
                back_track(path)  # 递归调用
                path.pop()  # 回溯，移除当前元素

        result = []
        back_track([])  # 初始调用，path为空
        return result

# 测试代码
nums = [1, 2, 3]
solution = Solution()
print(solution.permute(nums))
