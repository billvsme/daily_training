# coding: utf-8
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = None
        for num in nums:
            if count == 0:
                res = num

            count += 1 if res == num else -1

        return res


nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
