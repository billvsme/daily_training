# coding: utf-8
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(candidates, path, target, start):
            total = sum(path)
            if total == target:
                res.append(path[:])
                return
            elif total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(candidates, path, target, i)
                path.pop()

        backtrack(candidates, [], target, 0)

        return res


candidates = [2, 3, 6, 7]
target = 7

print(Solution().combinationSum(candidates, target))
