# coding: utf-8
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0
        max_index = 0

        n = len(nums)
        for i in range(n-1):
            max_index = max(max_index, i + nums[i])
            if i == end:
                end = max_index
                step += 1

        return step


print(Solution().jump([2,3,1,1,4]))
