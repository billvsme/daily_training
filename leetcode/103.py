# coding: utf-8
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        rest = []
        tag = True
        while queue:
            n = len(queue)
            item = []
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if tag:
                    item.append(node.val)
                else:
                    item.insert(0, node.val)

            rest.append(item)

            tag = not tag

        return rest
