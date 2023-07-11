# coding: utf-8
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        res = [[0]*n for _ in range(m)]

        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        res[i][j] = 1
                    else:
                        res[i][j] = min(res[i-1][j], res[i][j-1], res[i-1][j-1]) + 1

                    if res[i][j] > max_side:
                        max_side = res[i][j]

        return max_side * max_side


matrix = [["0","1"],["1","0"]]
print(Solution().maximalSquare(matrix))
