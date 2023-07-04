# coding: utf-8
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hash_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def dfs(index, temp):
            nonlocal digits, hash_map

            if index == len(digits):
                result.append(temp)
                return

            for c in hash_map[digits[index]]:
                dfs(index+1, temp+c)

        dfs(0, "")

        return result


digits = "23"
print(Solution().letterCombinations(digits))
