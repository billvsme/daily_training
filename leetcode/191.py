# coding: utf-8

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(c == "1" for c in "{:b}".format(n))
