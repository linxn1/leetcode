from typing import List


def can_go_round(point, gas, cost):
    gas_sum = 0
    count = len(gas)
    ans = -1
    while count > 0:
        gas_sum = gas_sum + gas[point] - cost[point]
        if gas_sum < 0:
            return ans
        else:
            point = (point + 1) % len(gas)
            count -= 1
    return point


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            ans = can_go_round(i, gas, cost)
            if ans != -1:
                return ans
        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))
