# coding: utf-8

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        res = [""] * numRows

        i, j, flag = 0, 0, -1
        for i in range(len(s)):
            if j == 0 or j == numRows - 1:
                flag = - flag

            res[j] += s[i]
            j += flag
            j = j % numRows

        return "".join(res)


print(Solution().convert("PAYPALISHIRING", 4))
