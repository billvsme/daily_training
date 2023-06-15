# coding: utf-8
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)

            pre = None
            for _ in range(n):
                node = queue.popleft()
                if pre is None:
                    pre = node
                else:
                    pre.next = node
                    pre = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if pre:
                pre.next = None

        return root
