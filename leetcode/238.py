# coding: utf-8
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        a, b = 1, 1

        for i in range(1, n):
            a = a * nums[i-1]
            res[i] = a

        for i in range(0, n-1)[::-1]:
            b = b * nums[i+1]
            res[i] = res[i] * b

        return res


print(Solution().productExceptSelf([1,2,3,4]))
