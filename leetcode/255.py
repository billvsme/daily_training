# coding: utf-8
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        min_v = float('-inf')
        for i in range(len(preorder)):
            if preorder[i] < min_v:
                return False

            while stack and preorder[i] > stack[-1]:
                min_v = stack.pop()

            stack.append(preorder[i])

        return True
