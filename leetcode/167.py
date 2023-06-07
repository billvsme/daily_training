# coding: utf-8
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                return [i+1, j+1]


numbers = [2,7,11,15]
target = 9

print(Solution().twoSum(numbers, target))
