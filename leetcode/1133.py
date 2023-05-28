# coding: utf-8
from typing import List
from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hash_map = defaultdict(lambda :0)
        for n in nums:
            hash_map[n] += 1

        max_n = -1
        for n in nums:
            if hash_map[n] == 1 and n > max_n:
                max_n = n

        return max_n

print(Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
