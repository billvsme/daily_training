# coding: utf-8
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        res = 0
        for price in prices:
            res = max(res, price-min_)
            min_ = min(min_, price)

        return res

print(Solution().maxProfit([7,1,5,3,6,4]))
