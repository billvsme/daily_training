# coding: utf-8

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        ans = 0

        end = n - 1
        for i in range(n-1, -1, -1):
            if s[i] != " ":
                end = i
                break

        for i in range(end, -1, -1):
            if s[i] != " ":
                ans += 1
            else:
                break

        return ans


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
