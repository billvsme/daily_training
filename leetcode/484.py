# coding: utf-8
from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        last_i = -1
        res = [1]
        for i, c in enumerate(s):
            if c == 'I':
                res.append(i+2)
                last_i = i
            else:
                res.insert(last_i+1, i+2)

        return res


print(Solution().findPermutation("ID"))
