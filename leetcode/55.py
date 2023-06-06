# coding: utf-8
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_ = nums[0]
        for i in range(n):
            max_ = max(max_, nums[i]+i)
            if max_ <= i and i != n-1:
                return False
        return True


print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
