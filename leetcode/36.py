# coding: utf-8
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            storage = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in storage:
                    return False
                else:
                    storage.append(board[i][j])

        for j in range(9):
            storage = []
            for i in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in storage:
                    return False
                else:
                    storage.append(board[i][j])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                storage = []
                for x in range(0, 3):
                    for y in range(0, 3):
                        if board[i+x][j+y] == '.':
                            continue
                        elif board[i+x][j+y] in storage:
                            return False
                        else:
                            storage.append(board[i+x][j+y])

        return True

board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))
