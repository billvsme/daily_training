# coding: utf-8
from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, min_v, max_v =  0, arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            res = max(res, abs(arrays[i][0] - max_v))
            print(res, min_v, max_v)

            if arrays[i][0] < min_v:
                min_v = arrays[i][0]
            if arrays[i][-1] > max_v:
                max_v = arrays[i][-1]

            
        return max_v - min_v;

print(Solution().maxDistance([[1,4],[0,5]]))
