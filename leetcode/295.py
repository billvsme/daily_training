# coding: utf-8
from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.h_min = []
        self.h_max = []

    def addNum(self, num: int) -> None:
        if not self.h_min or num < -self.h_min[0]:
            heappush(self.h_min, -num)
            if len(self.h_max) + 1 < len(self.h_min):
                heappush(self.h_max, -heappop(self.h_min))
        else:
            heappush(self.h_max, num)
            if len(self.h_max) > len(self.h_min):
                heappush(self.h_min, -heappop(self.h_max))

    def findMedian(self) -> float:
        if len(self.h_min) > len(self.h_max):
            return -self.h_min[0]
        else:
            return (-self.h_min[0]+self.h_max[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
