# coding: utf-8
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, left, right):
            if len(s) == 2*n:
                res.append(s)
                return
            if left < n:
                s += "("
                backtrack(s, left+1, right)
                s = s[:-1]
            if right < left:
                s += ")"
                backtrack(s, left, right+1)
                s = s[:-1]

        backtrack("", 0, 0)
        return res


print(Solution().generateParenthesis(3))
