# coding: utf-8
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        n = len(intervals)
        return all(intervals[i][1] <= intervals[i+1][0] for i in range(n-1))


intervals = [[0,30],[5,10],[15,20]]
print(Solution().canAttendMeetings(intervals))
