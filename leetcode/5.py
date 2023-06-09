# coding: utf-8

class Solution:
    def judge(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.judge(s, i, i)
            left2, right2 = self.judge(s, i, i+1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start: end+1]


print(Solution().longestPalindrome("abccbaaa"))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        max_len = 1
        res = s[0]

        for i in range(n):
            dp[i][i] = True

        for l in range(2, n+1):
            for i in range(n):
                j = i + l - 1
                if j > n-1:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if l == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and l > max_len:
                    res = s[i:j+1]

        return res


print(Solution().longestPalindrome("abccbaaa"))
