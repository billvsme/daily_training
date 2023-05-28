# coding: utf-8

from typing import List
from collections import defaultdict


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        hash_map_i = defaultdict(lambda :0)
        hash_map_j = defaultdict(lambda :0)
        ans = 0

        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    hash_map_i[i] += 1
                    hash_map_j[j] += 1

        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and hash_map_i[i] == 1 and hash_map_j[j] == 1:
                    ans += 1

        return ans


picture = [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]

print(Solution().findLonelyPixel(picture))
