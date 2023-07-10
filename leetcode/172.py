# coding: utf-8

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                ans += 1
                i = i // 5

        return ans


print(Solution().trailingZeroes(5))
