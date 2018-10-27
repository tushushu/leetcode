# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-27 09:18:26
@Last Modified by:   tushushu
@Last Modified time: 2018-10-27 09:18:26
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def __str__(self):
        nd = self.head
        ret = []
        for _ in range(self.length):
            ret.append(nd.val)
            nd = nd.next
        return str(ret)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.length:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = self.head
        if node is None:
            self.head = Node(val)
        else:
            for _ in range(self.length - 1):
                node = node.next
            node.next = Node(val)
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
        else:
            if index == 0:
                self.addAtHead(val)
            else:
                nd_pre = None
                nd_cur = self.head
                for _ in range(index):
                    nd_pre = nd_cur
                    nd_cur = nd_cur.next
                node = Node(val)
                nd_pre.next = node
                node.next = nd_cur
                self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.length:
            return
        nd_cur = self.head
        if index == 0:
            self.head = self.head.next
        else:
            nd_pre = None
            for _ in range(index):
                nd_pre = nd_cur
                nd_cur = nd_cur.next
            nd_pre.next = nd_cur.next
        self.length -= 1
