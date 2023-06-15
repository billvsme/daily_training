# coding: utf-8
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        cur_head = ListNode()
        cur = cur_head
        t = 0

        while cur1 and cur2:
            total = cur1.val + cur2.val + t
            cur.next = ListNode(total % 10)
            t = int(total / 10)

            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next

        while cur1:
            total = cur1.val + t
            cur.next = ListNode(total % 10)
            t = int(total / 10)
            cur1 = cur1.next
            cur = cur.next

        while cur2:
            total = cur2.val + t
            cur.next = ListNode(total % 10)
            t = int(total / 10)
            cur2 = cur2.next
            cur = cur.next

        if t:
            cur.next = ListNode(val=t)

        return cur_head.next
