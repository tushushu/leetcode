# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-11-07 11:47:23
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        ret = ListNode(0)
        ret.next = head
        last = ret
        node = head
        while node is not None and node.next is not None:
            next_node = node.next
            node.next = node.next.next
            next_node.next = node
            last.next = next_node
            last = node
            node = node.next
        return ret.next
