# coding: utf-8
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if (not left) ^ (not right):
                return False
            if left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
"""


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()

        queue.append(root.left)
        queue.append(root.right)

        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not left and not right:
                continue

            if (not left) ^ (not right):
                return False

            if left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(right.left)
            queue.append(left.right)

        return True
