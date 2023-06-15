# coding: utf-8
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def resvert(self, pre_start, k):
        start = pre_start.next

        pre = start
        cur = pre.next
        pre.next = None

        for _ in range(k-1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        pre_start.next = pre
        start.next = cur

        return start

    def list_len(self, head):
        cur = head
        ans = 0
        while cur:
            ans += 1
            cur = cur.next

        return ans

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre_head = ListNode()
        pre_head.next = head

        pre_start = pre_head

        while pre_start and self.list_len(pre_start.next) >= k:
            pre_start = self.resvert(pre_start, k)

        return pre_head.next
