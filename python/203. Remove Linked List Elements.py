# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-21 11:34:09
@Last Modified by:   tushushu
@Last Modified time: 2018-11-21 11:34:09
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if head is None:
            return head
        node_pre = head
        node_cur = head.next
        while node_cur:
            if node_cur.val == val:
                node_pre.next = node_cur.next
            else:
                node_pre = node_cur
            node_cur = node_cur.next
        return head
