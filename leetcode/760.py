# coding: utf-8
from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        b_map = {v: i for i, v in enumerate(nums2)}
        return [b_map[k] for k in nums1]


A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

print(Solution().anagramMappings(A, B))
