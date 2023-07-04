# coding: utf-8
from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n, m = len(board), len(board[0])

        def dfs(board, i, j):
            if not 0 <= i < n or not 0 <= j < m or board[i][j] != 'O':
                return
            board[i][j] = 'A'
            dfs(board, i+1, j)
            dfs(board, i, j+1)
            dfs(board, i-1, j)
            dfs(board, i, j-1)

        for i in range(n):
            dfs(board, i, 0)
            dfs(board, i, m-1)

        for j in range(m):
            dfs(board, 0, j)
            dfs(board, n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n, m = len(board), len(board[0])

        def bfs(board, i, j):
            queue = deque()
            queue.append((i, j))

            while queue:
                i, j = queue.popleft()

                if 0 <= i < n and 0 <= j < m and board[i][j] == 'O':
                    board[i][j] = 'A'
                    queue += [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]

        for i in range(n):
            bfs(board, i, 0)
            bfs(board, i, m-1)

        for j in range(m):
            bfs(board, 0, j)
            bfs(board, n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Solution2().solve(board)
print(board)
