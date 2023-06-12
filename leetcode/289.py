# coding: utf-8
import numpy as np
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        kernel = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        m = len(board)
        n = len(board[0])

        board_exp = np.array([[0]*(n+2) for _ in range(m+2)])
        board_exp[1:m+1, 1:n+1] = np.array(board)

        for i in range(1, m+1):
            for j in range(1, n+1):
                count = np.sum(kernel * board_exp[i-1:i+2, j-1:j+2])
                if board[i-1][j-1] == 1:
                    if count < 2 or count > 3:
                        board[i-1][j-1] = 0
                else:
                    if count == 3:
                        board[i-1][j-1] = 1

        return board


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(Solution().gameOfLife(board))
