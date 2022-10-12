# coding: utf-8

class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

def rev(head):
    pre = head
    cur = head.next
    head.next = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    return pre

def swap(head):
    if head is not None and head.next is not None:
        next_ = head.next
        head.next = swap(next_.next)
        next_.next = head
        return next_
    return head

def build_link(data):
    head = Node(data[0])
    node = head
    for item in data[1:]:
        node.next = Node(item)
        node = node.next

    return head

def print_link(head):
    rest, node = [], head
    while node:
        rest.append(node.data)
        node = node.next

    print(rest)

def link_code():
    head = build_link([1,2,3,4,5,6,7])
    print_link(head)
    head = rev(head)
    print_link(head)
    head = rev(head)
    print_link(head)
    head = swap(head)
    print_link(head)

if __name__ == '__main__':
    link_code()

