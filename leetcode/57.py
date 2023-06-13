# coding: utf-8
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        left, right = newInterval
        inserted = False

        for start, end in intervals:
            if end < left:
                res.append([start, end])
            elif right < start:
                if not inserted:
                    res.append([left, right])
                    inserted = True

                res.append([start, end])
            else:
                left = min(left, start)
                right = max(right, end)

        if not inserted:
            res.append([left, right])

        return res


intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().insert(intervals, newInterval))
