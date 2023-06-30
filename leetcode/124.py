# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.rest = -float("inf")

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            val = max(left + node.val, right + node.val, node.val)

            self.rest = max(self.rest, val, left + right + node.val)

            return val

        dfs(root)

        return self.rest
