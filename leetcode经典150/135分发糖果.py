from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candy = [1] * length
        # 两次遍历
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
            else:
                candy[i] = 1
        for i in reversed(range(length - 1)):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        print(candy)
        return sum(candy)


print(Solution().candy([1, 0, 2]))
