# coding: utf-8
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for i in range(1, n):
            if ratings[n-i-1] > ratings[n-i]:
                right[n-i-1] = right[n-i] + 1

        count = 0

        for i in range(n):
            count += max(left[i], right[i])

        return count


print(Solution().candy([1, 0, 2]))
