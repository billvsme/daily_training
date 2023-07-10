# coding: utf-8
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != float("inf") else -1


coins = [1, 2, 5]
amount = 11

print(Solution().coinChange(coins, amount))
