from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hindex = 0
        for i in range(len(citations)):
            if citations[i] > hindex:
                hindex += 1
        return hindex


citations = [3, 0, 6, 1, 5]
print(Solution().hIndex(citations))
