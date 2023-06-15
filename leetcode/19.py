# coding: utf-8
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        pre_head = ListNode()
        pre_head.next = head
        pre_del_cur = pre_head

        while cur:
            if n <= 0:
                pre_del_cur = pre_del_cur.next
            cur = cur.next
            n -= 1

        pre_del_cur.next = pre_del_cur.next.next
        return pre_head.next
