# coding: utf-8
from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque()
        queue.append((startGene, 0))

        while queue:
            cur, step = queue.popleft()
            for i, c1 in enumerate(cur):
                for c2 in 'ACGT':
                    if c1 != c2:
                        next_ = cur[:i] + c2 + cur[i+1:]
                        if next_ in bank:
                            if next_ == endGene:
                                return step + 1
                            bank.remove(next_)
                            queue.append((next_, step + 1))

        return -1


start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

print(Solution().minMutation(start, end, bank))
