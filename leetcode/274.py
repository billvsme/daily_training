# coding: utf-8
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)

        print(sorted_citations)

        i = 0
        h = 0
        while i < len(sorted_citations):

            c = sorted_citations[i]
            if c < i+1:
                break
            i += 1
            h += 1

        return h


print(Solution().hIndex([3,0,6,1,5]))
