# coding: utf-8
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        path = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue

                if i == 0 and j == 0:
                    path[i][j] = 1
                elif i == 0:
                    path[i][j] = path[i][j-1]
                elif j == 0:
                    path[i][j] = path[i-1][j]
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]

        return path[-1][-1]


obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))
