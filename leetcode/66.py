# coding: utf-8
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        t = 1
        for i in range(n):
            digits[n-i-1] += t
            if digits[n-i-1] == 10:
                digits[n-i-1] = 0
                t = 1
            else:
                t = 0
                break

        if t:
            digits.insert(0, 1)

        return digits


print(Solution().plusOne([9]))
