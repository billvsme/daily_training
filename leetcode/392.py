# coding: utf-8

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        if n == 0:
            return True

        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
                if i == n:
                    return True

        return i == len(s)


s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
