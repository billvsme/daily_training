# coding: utf-8
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        pre_small_head = ListNode()
        pre_large_head = ListNode()

        cur = head
        small_cur = pre_small_head
        large_cur = pre_large_head
        while cur:
            if cur.val < x:
                small_cur.next = ListNode(cur.val)
                small_cur = small_cur.next
            else:
                large_cur.next = ListNode(cur.val)
                large_cur = large_cur.next

            cur = cur.next

        small_cur.next = pre_large_head.next

        return pre_small_head.next
