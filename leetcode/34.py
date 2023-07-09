# coding: utf-8
from typing import List

class Solution:
    def searchLeft(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right -= 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return right + 1

    def searchRight(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left += 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        return [-1, -1] if left > right else [left, right]


nums = [5,7,7,8,8,10]
target = 8

print(Solution().searchRange(nums, target))
