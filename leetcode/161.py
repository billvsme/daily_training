# coding: utf-8

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False

        found_diff = False
        for i, (x, y) in enumerate(zip(s, t)):
            if x != y:
                found_diff = True
                return s[i+1:] == t[i+1:] if m == n else s[i:] == t[i+1:]

        return found_diff or n - m == 1


print(Solution().isOneEditDistance("a", "A"))
