class Solution:
    def intToRoman(self, num: int) -> str:
        unit = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # 下标所对应的元素即个位表示的罗马字符
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # 下标所对应的元素即十位表示的罗马字符
        hund = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # 下标所对应的元素即百位表示的罗马字符
        thou = ["", "M", "MM", "MMM"]  # 下标所对应的元素即千位表示的罗马字符
        return thou[num // 1000] + hund[num % 1000 // 100] + tens[num % 100 // 10] + unit[num % 10]


s = 3749
print(Solution().intToRoman(s))
