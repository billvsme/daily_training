# coding: utf-8
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre_head = ListNode(0)
        pre_head.next = head
        pre_start = pre_head
        for _ in range(left-1):
            pre_start = pre_start.next

        start = pre_start.next
        pre = start
        cur = pre.next
        start.next = None

        for _ in range(right-left):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        start.next = cur
        pre_start.next = pre

        return pre_head.next
