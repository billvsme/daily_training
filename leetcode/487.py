# coding: utf-8
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len, start = 0, 0
        a, b = 0, 0
        has_zero = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                a = b
                b = 0
                start = end + 1
                has_zero = 1
            else:
                b = end - start + 1

            max_len = max(max_len, a + b + has_zero)

        return max_len

print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
