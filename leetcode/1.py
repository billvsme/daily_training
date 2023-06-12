# coding: utf-8
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, value in enumerate(nums):
            dec = target - value
            if dec in hash_map:
                return [i, hash_map[dec]]
            hash_map[value] = i


nums = [2,7,11,15]
target = 9

print(Solution().twoSum(nums, target))
