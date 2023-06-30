# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_depth = 0
            left_node = node
            while left_node:
                left_node = left_node.left
                left_depth += 1

            right_depth = 0
            right_node = node
            while right_node:
                right_node = right_node.right
                right_depth += 1

            if left_depth == right_depth:
                return 2**right_depth - 1

            return dfs(node.left) + dfs(node.right) + 1

        return dfs(root)
