# coding: utf-8
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.rest = 0

        def dfs(node, number):
            if not node:
                return None
            if not node.left and not node.right:
                self.rest += int(str(number) + str(node.val))

            dfs(node.left, int(str(number) + str(node.val)))
            dfs(node.right, int(str(number) + str(node.val)))

        dfs(root, 0)
        return self.rest


class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        rest = 0
        queue.append((root, root.val))
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                rest += val

            if node.left:
                queue.append((node.left, int(str(val) + str(node.left.val))))
            if node.right:
                queue.append((node.right, int(str(val) + str(node.right.val))))

        return rest
