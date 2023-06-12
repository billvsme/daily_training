# coding: utf-8
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        max_len = 0
        for num in nums:
            if num not in hash_map:
                left = hash_map.get(num-1, 0)
                right = hash_map.get(num+1, 0)

                cur_len = 1 + left + right
                max_len = max(cur_len, max_len)
                hash_map[num] = cur_len
                hash_map[num-left] = cur_len
                hash_map[num+right] = cur_len

        return max_len


nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums))
