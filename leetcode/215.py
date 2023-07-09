# coding: utf-8
from typing import List

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)

        return h[0]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
