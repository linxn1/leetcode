class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        fast_p = 1
        low_p = 0
        num_sum = dict1[s[0]]
        while fast_p < len(s):
            num_sum += dict1[s[fast_p]]
            if s[low_p:fast_p + 1] == 'IV' or s[low_p:fast_p + 1] == 'IX':
                num_sum -= 2
            if s[low_p:fast_p + 1] == 'XL' or s[low_p:fast_p + 1] == 'XC':
                num_sum -= 20
            if s[low_p:fast_p + 1] == 'CD' or s[low_p:fast_p + 1] == 'CM':
                num_sum -= 200
            fast_p += 1
            low_p += 1
            print(num_sum)
        return num_sum


s = "MCMXCIV"
print(Solution().romanToInt(s))
