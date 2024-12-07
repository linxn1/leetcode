class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '' or len(s) == 1:
            return True

        string = ''
        for i in s:
            if i.isalpha() or i.isdecimal():
                string += i.lower()
        print(string)
        for i in range(int(len(string) / 2)):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True


s = "0P"
print(Solution().isPalindrome(s))
