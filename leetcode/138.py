# coding: utf-8
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        new_pre_head = Node(0)
        new_cur = new_pre_head
        cur = head
        while cur:

            new_cur.next = Node(cur.val)
            hash_map[cur] = new_cur.next

            cur = cur.next
            new_cur = new_cur.next

        cur = head
        new_cur = new_pre_head.next
        while cur:
            new_cur.random = hash_map[cur.random] if cur.random else None
            cur = cur.next
            new_cur = new_cur.next

        return new_pre_head.next
