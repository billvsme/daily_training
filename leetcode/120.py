# coding: utf-8
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)

        dp = [[0]*len(items) for items in triangle]
        dp[0][0] = triangle[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + triangle[i][0]

            k = len(triangle[i])

            for j in range(1, k-1):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

            dp[i][k-1] = dp[i-1][k-2] + triangle[i][k-1]

        return min(dp[-1])


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))
