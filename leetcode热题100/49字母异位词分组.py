from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictlist = {}
        for i in strs:
            key = str(sorted(i))
            if key in dictlist:
                dictlist[key].append(i)
            else:
                dictlist[key] = []
                dictlist[key].append(i)
        list1 = []
        for key, value in dictlist.items():
            list1.append(value)
        return list1


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
