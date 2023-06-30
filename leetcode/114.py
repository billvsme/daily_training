# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack, node = [], root
        rest = []
        while node or stack:
            while node:
                stack.append(node)

                rest.append(node)

                pre_node = node
                node = node.left

            node = stack.pop()
            node = node.right

        pre_node = None
        for node in rest:
            node.left = None
            if pre_node:
                pre_node.right = node
            pre_node = node
