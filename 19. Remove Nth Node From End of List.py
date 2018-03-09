# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:04:15 2018

@author: Administrator
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        if n == len(nodes):
            head = head.next
        else:
            nodes[-(n+1)].next = nodes[-n].next
        return head
