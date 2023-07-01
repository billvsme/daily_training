# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack, node = [], root
        rest = []
        min_desc = float("inf")
        pre_val = None
        while node or stack:
            while node:
                stack.append(node)

                node = node.left

            node = stack.pop()

            rest.append(node.val)
            if pre_val is not None:
                min_desc = min(min_desc, abs(node.val - pre_val))

            pre_val = node.val
            node = node.right

        return min_desc
