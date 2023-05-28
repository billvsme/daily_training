# coding: utf-8
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        heap = []

        heapq.heappush(heap, intervals[0][1])

        for start, end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)


intervals = [[0,30],[5,10],[15,20]]
print(Solution().minMeetingRooms(intervals))
