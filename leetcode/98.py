# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, node = [], root

        pre_val = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if pre_val is not None and node.val <= pre_val:
                return False

            pre_val = node.val
            node = node.right

        return True


class Solution2:
    def __init__(self):
        self.pre_val = float("-inf")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if root.val <= self.pre_val:
            return False

        self.pre_val = root.val

        return self.isValidBST(root.right)
