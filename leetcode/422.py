# coding: utf-8
from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except Exception:
                    return False

        return True


print(Solution().validWordSquare(["abcd", "bnrt", "crm", "dt"]))
