# coding: utf-8


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)

        return s[:n//2] == s[:-(n//2)-1:-1]
