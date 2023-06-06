# coding: utf-8
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            dec = prices[i] - prices[i-1]
            if dec > 0:
                res += dec

        return res


print(Solution().maxProfit([7,1,5,3,6,4]))
