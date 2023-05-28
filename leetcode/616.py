# coding: utf-8
from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        mark = [False] * n

        for i in range(n):
            for w in words:
                if s[i:].startswith(w):
                    for j in range(i, i+len(w)):
                        mark[j] = True

        res = ""
        b = False
        for i in range(n):
            if mark[i] and not b:
                res += "<b>"
                b = True
            if not mark[i] and b:
                res += "</b>"
                b = False

            res += s[i]

        if b:
            res += "</b>"

        return res


s = "abcxyz123"
words = ["abc", "123"]

print(Solution().addBoldTag(s, words))
