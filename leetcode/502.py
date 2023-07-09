# coding: utf-8
from typing import List
from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        items = sorted(zip(profits, capital), key=lambda x: x[1])

        i = 0
        cur = []

        while k > 0:
            while i < n and items[i][1] <= w:
                heappush(cur, -items[i][0])
                i += 1

            if cur:
                w -= heappop(cur)

            k -= 1

        return w


k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

print(Solution().findMaximizedCapital(k, w, profits, capital))
