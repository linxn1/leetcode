from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num = [None, None]
        for i in range(len(numbers)):
            target_num = target - numbers[i]
            for j in reversed(range(len(numbers))):
                if numbers[j] == target_num:
                    if i == j:
                        continue
                    num = [j + 1, i + 1]
                    break
        return num


print(Solution().twoSum([2, 3, 4], 6))
