class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        string = ''
        # 输出头
        for i in range(len(s)):
            if i % (2 * numRows - 2) == 0:
                string += s[i]

        # 输出中间
        # 设置余数
        for mod_num in range(1, numRows-1):
            for index in range(len(s)):
                if index % (2 * numRows - 2) == mod_num or index % (2 * numRows - 2) == 2 * numRows - 2 - mod_num:
                    string += s[index]

        # 输出尾
        for i in range(len(s)):
            if i % (2 * numRows - 2) == numRows - 1:
                string += s[i]
        return string


s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows))
