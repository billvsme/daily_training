# coding: utf-8
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]

        nums = [lower-1] + nums + [upper+1]

        res = []
        n = len(nums)

        for i in range(n-1):
            if nums[i+1] - nums[i] > 1:
                a = nums[i]+1
                b = nums[i+1]-1
                res.append([a, b])

        return res


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99

print(Solution().findMissingRanges(nums, lower, upper))
