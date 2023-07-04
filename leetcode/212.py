# coding: utf-8
import collections
from typing import List


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        current = root
        for word in words:
            for c in word:
                current = current.children[c]
            current.isword = True
            current = root

        n, m = len(board), len(board[0])

        result = []

        def dfs(board, root, word, i, j):
            if not 0 <= i < n or not 0 <= j < m or board[i][j] == '#':
                return

            current = root.children.get(board[i][j])
            if current is None:
                return

            word += board[i][j]
            if current.isword and word not in result:
                result.append(word)

            temp = board[i][j]
            board[i][j] = "#"
            dfs(board, current, word, i + 1, j)
            dfs(board, current, word, i, j + 1)
            dfs(board, current, word, i - 1, j)
            dfs(board, current, word, i, j - 1)
            board[i][j] = temp

        for i in range(n):
            for j in range(m):
                dfs(board, root, "", i, j)

        return result
