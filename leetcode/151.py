# coding: utf-8

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


print(Solution().reverseWords("the sky  is  blue   "))
