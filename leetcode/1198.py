# coding: utf-8

from typing import List
from collections import defaultdict


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        hash_map = defaultdict(lambda :0)
        for j in range(n):
            for i in range(m):
                hash_map[mat[i][j]] += 1
                if hash_map[mat[i][j]] == m:
                    return mat[i][j]

        return -1


mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(Solution().smallestCommonElement(mat))
