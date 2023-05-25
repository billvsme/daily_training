# coding: utf-8
from typing import List

class Solution:
    def reverve(self, s, i, j):
        for k in range(i, (i+j)//2):
            s[k], s[j-1-k+i] = s[j-1-k+i], s[k]

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        for j in range(len(s)):
            if s[j] != " ":
                continue
            self.reverve(s, i, j)
            i = j + 1
        
        self.reverve(s, i, len(s))
        self.reverve(s, 0, len(s))


s =  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Solution().reverseWords(s)

print(s)
