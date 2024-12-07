class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        list1 = [0, 1, 2]
        for i in range(3, n + 1):
            list1.append(list1[i - 2] + list1[i - 1])
        return list1[n]
