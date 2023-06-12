# coding: utf-8
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])

        visited = [[False] * n for _ in range(m)]
        res = []

        t = 0
        i, j = 0, 0
        for _ in range(m*n):
            res.append(matrix[i][j])
            visited[i][j] = True

            di, dj = direction[t]
            if i + di >= m or i + di < 0 or j + dj >= n or j + dj < 0 or visited[i+di][j+dj] is True:
                t = (t+1) % 4
                di, dj = direction[t]

            i += di
            j += dj

        return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(Solution().spiralOrder(matrix))
