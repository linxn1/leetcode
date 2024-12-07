class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        if len(string) == 1:
            return True

        for i in range(int(len(string) / 2)):
            if string[i] != string[len(string) - 1 - i]:
                return False
        return True


print(Solution().isPalindrome(121))
