# coding: utf-8
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


nums = [3,4,5,1,2]

print(Solution().findMin(nums))
