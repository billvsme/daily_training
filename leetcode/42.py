# coding: utf-8
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [height[0]] * n
        right = [height[-1]] * n

        for i in range(1, n):
            left[i] = max(height[i], left[i-1])

        for i in range(2, n+1):
            right[n-i] = max(height[n-i], right[n-i+1])

        return sum([min(left[i], right[i]) - height[i] for i in range(n)])


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
