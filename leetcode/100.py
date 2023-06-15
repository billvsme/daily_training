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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        if not q and p:
            return False
        if not q and not p:
            return True

        queue1, queue2 = deque(), deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False

            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False

            queue1.append(left1) if left1 else None
            queue1.append(right1) if right1 else None

            queue2.append(left2) if left2 else None
            queue2.append(right2) if right2 else None

        return not queue1 and not queue2
