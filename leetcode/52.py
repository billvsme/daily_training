# coding: utf-8


class Solution:
    def totalNQueens(self, n: int) -> int:
        col, pos, neg = set(), set(), set()

        res = 0

        def backtrack(i):
            nonlocal res
            if i == n:
                res += 1
                return
            else:
                for j in range(n):
                    if j not in col and i - j not in pos and i + j not in neg:
                        col.add(j)
                        pos.add(i - j)
                        neg.add(i + j)
                        backtrack(i+1)
                        col.remove(j)
                        pos.remove(i-j)
                        neg.remove(i+j)

        backtrack(0)
        return res


print(Solution().totalNQueens(4))
