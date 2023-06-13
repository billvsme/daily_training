# coding: utf-8
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda item: item[1])

        ans = 1
        t = points[0][1]
        for start, end in points[1:]:
            if t < start:
                ans += 1
                t = end

        return ans


print(Solution().findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
