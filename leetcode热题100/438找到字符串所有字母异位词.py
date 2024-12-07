from typing import List


def isyiwei(param, p):
    dict_para = {}
    dict_p = {}
    for i in param:
        if i not in dict_para.keys():
            dict_para[i] = 1
        else:
            dict_para[i] += 1
    for i in p:
        if i not in dict_p.keys():
            dict_p[i] = 1
        else:
            dict_p[i] += 1
    for i in dict_para.keys():
        if set(dict_p.keys()) != set(dict_para.keys()):
            return False
        if dict_para[i] != dict_p[i]:
            return False
    return True


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        list1 = []
        for i in range(len(s) - len(p) + 1):
            if isyiwei(s[i:i + p_len], p):
                list1.append(i)
        return list1


s = "ababababab"
p = "aab"
print(Solution().findAnagrams(s, p))
