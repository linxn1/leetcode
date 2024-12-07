class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        magazine_dict = {}
        for i in ransomNote:
            if i not in ransomNote_dict.keys():
                ransomNote_dict[i] = 1
            else:
                ransomNote_dict[i] += 1
        for i in magazine:
            if i not in magazine_dict.keys():
                magazine_dict[i] = 1
            else:
                magazine_dict[i] += 1

        print(ransomNote_dict)
        print(magazine_dict)

        for i in ransomNote_dict.keys():
            if i not in magazine_dict.keys():
                return False
            if ransomNote_dict[i] > magazine_dict[i]:
                return False
        return True


ransomNote = "a"
magazine = "b"
Solution().canConstruct(ransomNote, magazine)
