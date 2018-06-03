<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:12:08 2018

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def cmp(self, l1, l2):
        if l2 is None:
            return True
        if l1 is None:
            return False
        return l1.val < l2.val

    def mergeTwoLists(self, l1, l2):
        if l1 == []:
            return l2
        if l2 == []:
            return l1
        node = ListNode(None)
        tmp = node
        while l1 or l2:
            if self.cmp(l1, l2):
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        return node.next
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:12:08 2018

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def cmp(self, l1, l2):
        if l2 is None:
            return True
        if l1 is None:
            return False
        return l1.val < l2.val

    def mergeTwoLists(self, l1, l2):
        if l1 == []:
            return l2
        if l2 == []:
            return l1
        node = ListNode(None)
        tmp = node
        while l1 or l2:
            if self.cmp(l1, l2):
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        return node.next
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
