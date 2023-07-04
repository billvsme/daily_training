# coding: utf-8
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m = len(board), len(board[0])

        def dfs(index, i, j):
            if index == len(word):
                return True

            if not 0 <= i < n or not 0 <= j < m or board[i][j] == "#" or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            a = dfs(index+1, i+1, j)
            b = dfs(index+1, i, j+1)
            c = dfs(index+1, i-1, j)
            d = dfs(index+1, i, j-1)

            board[i][j] = temp

            if a or b or c or d:
                return True
            else:
                return False

        for i in range(n):
            for j in range(m):
                if dfs(0, i, j):
                    return True

        return False



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(Solution().exist(board, word))
