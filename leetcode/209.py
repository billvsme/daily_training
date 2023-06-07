# coding: utf-8
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        n = len(nums)
        total = 0
        res = n + 1
        while end < n:
            total += nums[end]
            while total >= target:
                res = min(res, end-start+1)
                total -= nums[start]
                start += 1

            end += 1

        return res if res != n + 1 else 0


target = 7
nums = [2,3,1,2,4,3]

print(Solution().minSubArrayLen(target, nums))
