# coding: utf-8
from typing import List
from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []

        m, n = len(nums1), len(nums2)
        h = [(nums1[i]+nums2[0], i, 0) for i in range(min(k, m))]

        while h and len(res) < k:
            _, i, j = heappop(h)

            res.append([nums1[i], nums2[j]])

            if j + 1 < n:
                heappush(h, (nums1[i]+nums2[j+1], i, j + 1))

        return res


nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

print(Solution().kSmallestPairs(nums1, nums2, k))
