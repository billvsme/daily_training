# coding: utf-8
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(n, k, path, start):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)
                backtrack(n, k, path, i+1)
                path.pop()

        backtrack(n, k, [], 1)

        return res


n = 4
k = 2

print(Solution().combine(n, k))
