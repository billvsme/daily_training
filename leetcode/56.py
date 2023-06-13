# coding: utf-8
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = [[intervals[0][0], intervals[0][1]]]

        for i in range(1, n):
            start, end = intervals[i]
            if res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))
