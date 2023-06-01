# coding: utf-8
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i


nums = [0,1,2,2,3,0,4,2]
val = 2

print(nums[:Solution().removeElement(nums, val)])
