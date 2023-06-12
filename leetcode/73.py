# coding: utf-8
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row0_flag = any(matrix[0][j] == 0 for j in range(n))
        col0_flag = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(n):
                matrix[0][j] = 0

        if col0_flag:
            for i in range(m):
                matrix[i][0] = 0

        return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeroes(matrix))
