# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:19:57 2018

@author: Administrator
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        stack = []
        p = q = head
        n = 0
        while p:
            if n < k and q:
                stack.append(q.val)
                q = q.next
                n += 1
            elif q is None and n < k:
                return head
            else:
                while stack:
                    p.val = stack.pop()
                    p = p.next
                n = 0
        return head
