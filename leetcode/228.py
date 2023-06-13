# coding: utf-8
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        nums.append(float("inf"))

        n = len(nums)
        start = nums[0]
        for i in range(1, n):
            if nums[i] != nums[i-1] + 1:
                if start != nums[i-1]:
                    res.append(f"{start}->{nums[i-1]}")
                else:
                    res.append(f"{start}")
                start = nums[i]

        return res


nums = [0,1,2,4,5,7]
print(Solution().summaryRanges(nums))
