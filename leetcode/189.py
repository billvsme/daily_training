# coding: utf-8
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:]+nums[:n-k]


nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)
