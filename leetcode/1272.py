# coding: utf-8
from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        left, right = toBeRemoved
        res = []
        for a, b in intervals:
            if b <= left or a >= right:
                res.append([a, b])
            else:
                if a < left:
                    res.append([a, left])
                if b > right:
                    res.append([right, b])

        return res


intervals = [[0, 5]]
toBeRemoved = [2, 3]

print(Solution().removeInterval(intervals, toBeRemoved))
