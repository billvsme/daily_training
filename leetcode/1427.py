# coding: utf-8
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        l = len(s)
        for i in range(len(shift)):
            direction, amount = shift[i][0], shift[i][-1]
            amount = amount % l
            if direction:
                s = s[l-amount:] + s[:l-amount]
            else:
                s = s[amount:] + s[:amount]

        return s


print(Solution().stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))
