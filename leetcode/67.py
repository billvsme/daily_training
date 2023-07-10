# coding: utf-8

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))


a = "1010"
b = "1011"
print(Solution().addBinary(a, b))
