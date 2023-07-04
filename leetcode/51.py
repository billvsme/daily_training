# coding: utf-8
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        col, pos, neg = set(), set(), set()

        def backtrack(i):
            nonlocal res

            if i == n:
                temp = [["."]*n for _ in range(n)]
                for x in range(n):
                    temp[x][queens[x]] = "Q"
                res.append(["".join(items) for items in temp])
                return
            else:
                for j in range(n):
                    if j not in col and i - j not in pos and i + j not in neg:
                        col.add(j)
                        pos.add(i - j)
                        neg.add(i + j)
                        queens[i] = j
                        backtrack(i + 1)
                        col.remove(j)
                        pos.remove(i - j)
                        neg.remove(i + j)

        queens = {}
        backtrack(0)

        return res


print(Solution().solveNQueens(4))
