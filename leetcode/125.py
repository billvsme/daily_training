# coding: utf-8

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
